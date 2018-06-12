# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from frontEnd.forms import *
from frontEnd.models import *
import datetime, pymysql, re
# Create your views here.

@login_required
def bedadddetails(request, bed_id):
    return render(request, 'add_bed_details.html', {'bed_id': bed_id})


@login_required
def addpeople(request, bed_id):
    form = PatientForm(request.POST)
    latest_patient = Patient.objects.filter(bed_number=bed_id).last()
    error_msg = '其他异常错误'
    # method = "POST"：1，当前未出院病人信息（修改或添加）
    #                  2，前一病人已出院，添加新病人
    if request.method == 'POST' and form.is_valid():
        try:
            #  入院时间 > 出院时间，报错
            if form.cleaned_data['in_date'] is not None and form.cleaned_data['out_date'] is not None \
                    and (form.cleaned_data['in_date'] > form.cleaned_data['out_date']):
                error_msg = '出院时间不能早于入院时间'
                raise Exception
            # 有出院时间没有入院时间，报错
            if form.cleaned_data['in_date'] is None and form.cleaned_data['out_date'] is not None:
                error_msg = '已出院病人必须填写入院时间'
                raise Exception
            newPatient = Patient(bed_number=bed_id, subject_id=form.cleaned_data['subject_id'],
                                 gender=form.cleaned_data['gender'], age=form.cleaned_data['age'],
                                 height=form.cleaned_data['height'], weight=form.cleaned_data['weight'],
                                 in_date=form.cleaned_data['in_date'], out_date=form.cleaned_data['out_date'],
                                 )
            # 上一病人必须出院才能添加新病人，否则异常报错
            if latest_patient is not None and latest_patient.out_date is None \
                    and newPatient.subject_id != latest_patient.subject_id:
                error_msg = '该床上一病人必须出院才能添加新病人'
                raise Exception
            # 提交病人信息已经存在：1，已经出院，异常报错
            #                   2，还未出院，修改或添加信息
            if Patient.objects.filter(bed_number=bed_id, subject_id=newPatient.subject_id).exists():
                print("exist")
                original_patient = Patient.objects.get(bed_number=bed_id, subject_id=newPatient.subject_id)
                if original_patient.out_date is not None:
                    error_msg = '该病号对应病人已经录入数据库，不能输入重复的病号信息。若修改，请登录管理员页面操作。'
                    raise Exception
                original_patient.gender = newPatient.gender
                original_patient.age = newPatient.age
                original_patient.height = newPatient.height
                original_patient.weight = newPatient.weight
                original_patient.in_date = newPatient.in_date
                original_patient.out_date = newPatient.out_date
                original_patient.save()
            # 提交新病人信息并保存
            else:
                newPatient.save()
            redirect_url = reverse('bedAddDetails', args=[bed_id, ])
            return HttpResponseRedirect(redirect_url)
        except:
            if latest_patient is not None and latest_patient.out_date is None:
                newForm = PatientForm(instance=latest_patient)
            else:
                newForm = PatientForm()
            return render(request, 'add_new_info.html', {'form': newForm,
                                                         'bed_id': bed_id,
                                                         'msg': '病人基本信息',
                                                         'error': error_msg})
    # method = "GET"： 1，当前病人还未出院，渲染旧表单
    #                  2，当前病人已出院，渲染新表单
    else:
        if latest_patient is not None and latest_patient.out_date is None:
            insuf_form = PatientForm(instance=latest_patient)
            return render(request, 'add_new_info.html', {'form': insuf_form,
                                                         'bed_id': bed_id,
                                                         'msg': '病人基本信息',
                                                         'error': '请填写该病床当前病人出院时间，方可录入新入院病人; 您也可以修改当前病人基本信息'})
        else:
            newForm = PatientForm()
            return render(request, 'add_new_info.html', {'form': newForm, 'bed_id': bed_id, 'msg': '病人基本信息'})


def add_old_people(request):
    return HttpResponseRedirect(reverse('homepage'))


@login_required
def addmedhistory(request, bed_id):
    form = PatientMHForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        # cur_bed = get_object_or_404(PatientBed, bed_ID=bed_id)
        newPatientMH = PatientMH.objects.create(
            bed_number=bed_id,
            subject_id=form.cleaned_data['subject_id'],
            inquiry_date=form.cleaned_data['inquiry_date'],
            past_history=form.cleaned_data['past_history'],
            personal_history=form.cleaned_data['personal_history'],
            family_history=form.cleaned_data['family_history'],
            in_symptom=form.cleaned_data['in_symptom'],
            out_symptom=form.cleaned_data['out_symptom'],
        )
        newPatientMH.save()
        redirect_url = reverse('bedAddDetails', args=[bed_id, ])
        return HttpResponseRedirect(redirect_url)
    else:
        newForm = PatientMHForm()
        return render(request, 'add_new_info.html', {'form': newForm, 'bed_id': bed_id, 'msg': '病史'})


@login_required
def adddaydiag(request, bed_id):
    form = PatientTEForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        # cur_bed = get_object_or_404(PatientBed, bed_ID=bed_id)
        newPatientTE = PatientTE.objects.create(
            bed_number=bed_id,
            subject_id=form.cleaned_data['subject_id'],
            exam_program=form.cleaned_data['exam_program'],
            result=form.cleaned_data['result'],
            date=form.cleaned_data['date'],
            all_result=form.cleaned_data['all_result'],
        )
        newPatientTE.save()
        redirect_url = reverse('bedAddDetails', args=[bed_id, ])
        return HttpResponseRedirect(redirect_url)
    else:
        newForm = PatientTEForm()
        return render(request, 'add_new_info.html', {'form': newForm, 'bed_id': bed_id, 'msg': '每日问诊'})


@login_required
def addradreport(request, bed_id):
    form = PatientLBForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        # cur_bed = get_object_or_404(PatientBed, bed_ID=bed_id)
        newPatientLB = PatientLB.objects.create(
            bed_number=bed_id,
            subject_id=form.cleaned_data['subject_id'],
            date=form.cleaned_data['date'],
            category=form.cleaned_data['category'],
            subcategory=form.cleaned_data['subcategory'],
            exam_program=form.cleaned_data['exam_program'],
            result=form.cleaned_data['result'],
        )
        newPatientLB.save()
        redirect_url = reverse('bedAddDetails', args=[bed_id, ])
        return HttpResponseRedirect(redirect_url)
    else:
        newForm = PatientLBForm()
        return render(request, 'add_new_info.html', {'form': newForm, 'bed_id': bed_id, 'msg': '化验放射检验报告'})


@login_required
def adddrughistory(request, bed_id):
    form = PatientEXForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        # cur_bed = get_object_or_404(PatientBed, bed_ID=bed_id)
        newPatientEX = PatientEX.objects.create(
            bed_number=bed_id,
            subject_id=form.cleaned_data['subject_id'],
            dose=form.cleaned_data['dose'],
            date=form.cleaned_data['date'],
        )
        newPatientEX.save()
        redirect_url = reverse('bedAddDetails', args=[bed_id, ])
        return HttpResponseRedirect(redirect_url)
    else:
        newForm = PatientEXForm()
        return render(request, 'add_new_info.html', {'form': newForm, 'bed_id': bed_id, 'msg': '用药记录'})


@login_required
def addsurghistory(request, bed_id):
    form = PatientPRForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        # cur_bed = get_object_or_404(PatientBed, bed_ID=bed_id)
        newPatientPR = PatientPR.objects.create(
            bed_number=bed_id,
            subject_id=form.cleaned_data['subject_id'],
            is_operated=form.cleaned_data['is_operated'],
            category=form.cleaned_data['category'],
            date=form.cleaned_data['date'],
        )
        newPatientPR.save()
        redirect_url = reverse('bedAddDetails', args=[bed_id, ])
        return HttpResponseRedirect(redirect_url)
    else:
        newForm = PatientPRForm()
        return render(request, 'add_new_info.html', {'form': newForm, 'bed_id': bed_id, 'msg': '用药记录'})


@login_required
def addbodystatus(request, bed_id):
    form = PatientPEForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        # cur_bed = get_object_or_404(PatientBed, bed_ID=bed_id)
        newPatientPE = PatientPE.objects.create(
            bed_number=bed_id,
            subject_id=form.cleaned_data['subject_id'],
            category=form.cleaned_data['category'],
            result=form.cleaned_data['result'],
            date=form.cleaned_data['date'],
        )
        newPatientPE.save()
        redirect_url = reverse('bedAddDetails', args=[bed_id, ])
        return HttpResponseRedirect(redirect_url)
    else:
        newForm = PatientPEForm()
        return render(request, 'add_new_info.html', {'form': newForm, 'bed_id': bed_id, 'msg': '体格检验'})


@login_required
def beddetail(request, bed_id):
    history_patients = Patient.objects.filter(bed_number=bed_id).order_by('-subject_id')
    return render(request, 'yiyuan_patient_display.html', {'patients': history_patients, 'bed_id': bed_id})


@login_required
def patientdetail(request, subject_id):
    cur_patient = Patient.objects.get(subject_id=subject_id)
    history_patients = Patient.objects.filter(bed_number=cur_patient.bed_number).order_by('-subject_id')
    # 得到最近一天日期和最多7天前
    recent_day = None
    start_day = cur_patient.in_date
    if cur_patient.out_date is None:
        recent_day = datetime.date.today() - datetime.timedelta(days=1)
    else:
        recent_day = cur_patient.out_date - datetime.timedelta(days=1)

    if recent_day - cur_patient.in_date > datetime.timedelta(days=7):
        start_day = recent_day - datetime.timedelta(days=7)
    start_day = start_day.strftime("%Y-%m-%d")
    recent_day = recent_day.strftime("%Y-%m-%d")
    try:
        conn = pymysql.connect("114.55.6.251", "root", "ad016dbbab", "test_LanDe", charset="utf8")
    except:
        print("Failed to connect to db test")
        return HttpResponseRedirect(reverse('homepage'))
    cur = conn.cursor()
    # 获取当天quality_duration 分割拼接时间以及对应睡眠质量值
    one_day_query = 'SELECT quality_duration FROM sleep_info as SI, yiyuan_beds as YB WHERE SI.device_id = YB.device_id AND YB.bed_ID = (%s) AND SI.date = (%s)'
    cur.execute(one_day_query, (cur_patient.bed_number, str(recent_day)+' 00:00:00'))
    recent_qd = cur.fetchone()
    recent_qd_str = str(recent_qd[0])
    print(recent_qd_str)
    row_time = []
    row_value = []
    data_snapshots = re.split(r'[,]', recent_qd_str)
    for row in data_snapshots:
        snapshot = re.split(r'[|]', row)
        if len(snapshot) is 2:
            row_time.append(snapshot[0])
            row_value.append(snapshot[1])
    # 获得最多7天其他健康数据
    seven_day_query = 'SELECT SI.date, deep_sleep, sleep_grade, major_heart_rate FROM sleep_info as SI, yiyuan_beds as YB ' \
                      'WHERE SI.device_id = YB.device_id AND YB.bed_ID = (%s) AND SI.date BETWEEN (%s) AND (%s)'
    cur.execute(seven_day_query, (cur_patient.bed_number, str(start_day)+' 00:00:00', str(recent_day)+' 00:00:00'))
    data_seven_days = cur.fetchall()
    # print(data_seven_days)
    dates = []
    deepSleeps = []
    sleepGrades = []
    majorHR = []
    for data_day in data_seven_days:
        dates.append(str(data_day[0].strftime("%Y-%m-%d")))
        deepSleeps.append(data_day[1])
        sleepGrades.append(data_day[2])
        majorHR.append(data_day[3])
    # print(dates)
    # print(deepSleeps)
    # print(sleepGrades)
    # print(majorHR)
    cur.close()
    conn.close()
    return render(request, 'yiyuan_patient_display.html', {'patients': history_patients, 'bed_id': cur_patient.bed_number,
                                                           'oneday_time': row_time, 'oneday_value': row_value, 'cur_patient': cur_patient,
                                                           'dates': dates, 'deepSleeps': deepSleeps, 'sleepGrades': sleepGrades, 'majorHR': majorHR})

@login_required
def singlePatientDetail(request, subject_id):
    cur_patient = Patient.objects.get(subject_id=subject_id)
    history_patients = Patient.objects.filter(bed_number=cur_patient.bed_number).order_by('-subject_id')
    # 得到最近一天日期和最多7天前
    recent_day = None
    start_day = cur_patient.in_date
    if cur_patient.out_date is None:
        recent_day = datetime.date.today() - datetime.timedelta(days=1)
    else:
        recent_day = cur_patient.out_date - datetime.timedelta(days=1)

    if recent_day - cur_patient.in_date > datetime.timedelta(days=7):
        start_day = recent_day - datetime.timedelta(days=7)
    start_day = start_day.strftime("%Y-%m-%d")
    recent_day = recent_day.strftime("%Y-%m-%d")
    try:
        conn = pymysql.connect("114.55.6.251", "root", "ad016dbbab", "test_LanDe", charset="utf8")
    except:
        print("Failed to connect to db test")
        return HttpResponseRedirect(reverse('homepage'))
    cur = conn.cursor()
    # 获取当天quality_duration 分割拼接时间以及对应睡眠质量值
    one_day_query = 'SELECT quality_duration FROM sleep_info as SI, yiyuan_beds as YB WHERE SI.device_id = YB.device_id AND YB.bed_ID = (%s) AND SI.date = (%s)'
    cur.execute(one_day_query, (cur_patient.bed_number, str(recent_day) + ' 00:00:00'))
    recent_qd = cur.fetchone()
    recent_qd_str = str(recent_qd[0])
    print(recent_qd_str)
    row_time = []
    row_value = []
    data_snapshots = re.split(r'[,]', recent_qd_str)
    for row in data_snapshots:
        snapshot = re.split(r'[|]', row)
        if len(snapshot) is 2:
            row_time.append(snapshot[0])
            row_value.append(snapshot[1])
    # 获得最多7天其他健康数据
    seven_day_query = 'SELECT SI.date, deep_sleep, sleep_grade, major_heart_rate FROM sleep_info as SI, yiyuan_beds as YB ' \
                      'WHERE SI.device_id = YB.device_id AND YB.bed_ID = (%s) AND SI.date BETWEEN (%s) AND (%s)'
    cur.execute(seven_day_query, (cur_patient.bed_number, str(start_day) + ' 00:00:00', str(recent_day) + ' 00:00:00'))
    data_seven_days = cur.fetchall()
    # print(data_seven_days)
    dates = []
    deepSleeps = []
    sleepGrades = []
    majorHR = []
    for data_day in data_seven_days:
        dates.append(str(data_day[0].strftime("%Y-%m-%d")))
        deepSleeps.append(data_day[1])
        sleepGrades.append(data_day[2])
        majorHR.append(data_day[3])
    # print(dates)
    # print(deepSleeps)
    # print(sleepGrades)
    # print(majorHR)
    cur.close()
    conn.close()
    return render(request, 'yiyuan_patient_single_display.html',
                  {'patients': history_patients, 'bed_id': cur_patient.bed_number,
                   'oneday_time': row_time, 'oneday_value': row_value, 'cur_patient': cur_patient,
                   'dates': dates, 'deepSleeps': deepSleeps, 'sleepGrades': sleepGrades, 'majorHR': majorHR,'subject_id':subject_id},)










