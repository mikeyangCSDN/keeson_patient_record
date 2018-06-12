# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from frontEnd.forms import *
from frontEnd.models import *
import pymysql
from django.contrib.auth.models import User
import re
from pyecharts import Bar, Line


@login_required
def homepage(request):
    cur_user = get_object_or_404(User, pk=request.user.id)
    if cur_user.username == "jiaxingyiyuan":
        form = BedForm(request.POST)
        bed_exist = False
        if request.method == 'POST' and form.is_valid():
            bed_exist = PatientBed.objects.filter(bed_ID=form.cleaned_data['bed_ID']).exists()
            if not bed_exist:
                PatientBed.objects.create(bed_ID=form.cleaned_data['bed_ID'])
        new_form = BedForm()
        bed_set = PatientBed.objects.all().order_by('bed_ID')
        return render(request, 'yiyuan_homepage.html', {'form': new_form, 'bed_set': bed_set, 'bed_exist': bed_exist})
        # try:
        #     conn = pymysql.connect("114.55.6.251", "root", "ad016dbbab", "test", charset="utf8")
        # except:
        #     print("Failed to connect to db test")
        #     return HttpResponseRedirect(reverse('home'))
        # cur = conn.cursor()
        # bed_query = "SELECT serial_number FROM sc_app_beds;"
        # cur.execute(bed_query)
        # rows = cur.fetchall()
        # cur.close()
        # conn.close()
        # return render(request, 'yiyuan_homepage.html', {'bed_set': rows})
    elif cur_user.username == "ronghua":
        try:
            conn = pymysql.connect("114.55.6.251", "root", "ad016dbbab", "institution_data", charset="utf8")
            print("conn succeeds")
        except:
            print("Failed to connect to db test")
            return HttpResponseRedirect(reverse('home'))
        cur = conn.cursor()
        bed_query = "SELECT serial_number FROM ronghua_beds;"
        cur.execute(bed_query)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return render(request, 'ronghua_homepage.html', {'bed_set': rows})

@login_required
def displaypage(request):
    cur_user = get_object_or_404(User, pk=request.user.id)
    if cur_user.username == "jiaxingyiyuan":
        bed_set = PatientBed.objects.all()
        return render(request, 'yiyuan_bed_set_display.html', {'bedSet': bed_set})
    elif cur_user.username == "ronghua":
        try:
            conn = pymysql.connect("114.55.6.251", "root", "ad016dbbab", "test", charset="utf8")
        except:
            print("Failed to connect to db softide_cloud2")
            return HttpResponseRedirect(reverse('homepage'))
        cur = conn.cursor()
        bedQuery = "SELECT id, device_id FROM sleep_info;"
        cur.execute(bedQuery)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return render(request, 'bed_page.html', {'bedSet': rows})


@login_required
def beddetail(request, device_id):
    try:
        conn = pymysql.connect("114.55.6.251", "root", "ad016dbbab", "test", charset="utf8")
    except:
        print("Failed to connect to db test")
        return HttpResponseRedirect(reverse('homepage'))
    cur = conn.cursor()
    bed_detail_query = "SELECT quality_duration  FROM sleep_info WHERE device_id = (%s);"
    cur.execute(bed_detail_query, (device_id,))
    rows = cur.fetchone()
    rows1 = str(rows)
    # print(isinstance(rows1, str))
    row_time = []
    row_value = []
    data_snapshots = re.split(r'[,]', rows1)
    # print(data_snapshots)
    # print(isinstance(data_snapshots, list))
    for row in data_snapshots:
        snapshot = re.split(r'[ |]', row)
        if len(snapshot) is 3:
            # print(snapshot)
            row_time.append(snapshot[1])
            row_value.append(snapshot[2])
    # print(row_time)
    # print(row_value)
    bar = Bar("当日睡眠质量折线图")
    bar.add("健康指数", row_time, row_value, mark_line=["average"], mark_point=["max", "min"])
    bar.render(r"frontEnd/templates/daily_quality_duration.html")
    cur.close()
    conn.close()
    return render(request, 'display_test_page.html')


@login_required
def display_test(request):
    try:
        conn = pymysql.connect("114.55.6.251", "root", "ad016dbbab", "test", charset="utf8")
    except:
        print("Failed to connect to db test")
        return HttpResponseRedirect(reverse('homepage'))
    cur = conn.cursor()
    bed_detail_query = "SELECT quality_duration  FROM sleep_info WHERE id = 1;"
    cur.execute(bed_detail_query)
    rows = cur.fetchone()
    rows1 = str(rows)
    # print(isinstance(rows1, str))
    row_time = []
    row_value = []
    data_snapshots = re.split(r'[,]', rows1)
    # print(data_snapshots)
    # print(isinstance(data_snapshots, list))
    for row in data_snapshots:
        snapshot = re.split(r'[ |]', row)
        if len(snapshot) is 3:
            # print(snapshot)
            row_time.append(snapshot[1])
            row_value.append(snapshot[2])
    # print(row_time)
    # print(row_value)
    bar = Bar("当日睡眠质量折线图")
    bar.add("健康指数", row_time, row_value, mark_line=["average"], mark_point=["max", "min"])
    bar.render(r"frontEnd/templates/daily_quality_duration.html")
    cur.close()
    conn.close()
    return render(request, 'display_test_page.html')


@login_required
def display_daily_info(request):
    return render(request, 'daily_quality_duration.html')