# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from frontEnd.forms import *
from frontEnd.models import *


@login_required
def bedadddetails(request, bed_id):
    return render(request, 'ronghua_add_bed_details.html', {'bed_id': bed_id})


@login_required
def addpeople(request, bed_id):
    form = DM_RonghuaForm(request.POST)
    latest_patient = DM_Ronghua.objects.filter(bed_number=bed_id).last()
    error_msg = '其他异常错误'
    # method = "POST"：1，当前未出院病人信息（修改或添加）
    #                  2，前一病人已出院，添加新病人
    if request.method == 'POST' and form.is_valid():
        try:
            if form.cleaned_data['in_date'] is not None and form.cleaned_data['out_date'] is not None \
                    and (form.cleaned_data['in_date'] > form.cleaned_data['out_date']):
                error_msg = '出院时间不能早于入院时间'
                raise Exception
            if form.cleaned_data['in_date'] is None and form.cleaned_data['out_date'] is not None:
                error_msg = '已出院养老院客户必须填写入院时间'
                raise Exception
            newPatient = DM_Ronghua(bed_number=bed_id, subject_id=form.cleaned_data['subject_id'],
                                    gender=form.cleaned_data['gender'], age=form.cleaned_data['age'],
                                    height=form.cleaned_data['height'], weight=form.cleaned_data['weight'],
                                    in_date=form.cleaned_data['in_date'], out_date=form.cleaned_data['out_date'],
                                    in_diagnose=form.cleaned_data['in_diagnose'])
            if latest_patient is not None and latest_patient.out_date is None \
                    and newPatient.subject_id != latest_patient.subject_id:
                error_msg = '该床上一养老院客户必须出院才能添加新客户'
                raise Exception
            if DM_Ronghua.objects.filter(bed_number=bed_id, subject_id=newPatient.subject_id).exists():
                print("exist")
                original_patient = DM_Ronghua.objects.get(bed_number=bed_id, subject_id=newPatient.subject_id)
                if original_patient.out_date is not None:
                    error_msg = '该客户号对应养老院客户已经录入数据库库，不能输入重复的病号信息。若修改，请登录管理员页面操作。'
                    raise Exception
                original_patient.gender = newPatient.gender
                original_patient.age = newPatient.age
                original_patient.height = newPatient.height
                original_patient.weight = newPatient.weight
                original_patient.in_date = newPatient.in_date
                original_patient.out_date = newPatient.out_date
                original_patient.in_diagnose = newPatient.in_diagnose
                original_patient.save()
            else:
                newPatient.save()
            redirect_url = reverse('bedAddDetailsRonghua', args=[bed_id, ])
            return HttpResponseRedirect(redirect_url)
        except:
            if latest_patient is not None and latest_patient.out_date is None:
                newForm = DM_RonghuaForm(instance=latest_patient)
            else:
                newForm = DM_RonghuaForm()
            return render(request, 'add_new_info.html', {'form': newForm,
                                                         'bed_id': bed_id,
                                                         'msg': '荣华养老院客户基本信息',
                                                         'error': error_msg})
    else:
        if latest_patient is not None and latest_patient.out_date is None:
            insuf_form = DM_RonghuaForm(instance=latest_patient)
            return render(request, 'add_new_info.html', {'form': insuf_form,
                                                         'bed_id': bed_id,
                                                         'msg': '荣华养老院客户基本信息',
                                                         'error': '请填写该床最近客户出院时间，方可添加新入院客户; 您也可以修改当前客户基本信息'})
        else:
            newForm = DM_RonghuaForm()
            return render(request, 'add_new_info.html', {'form': newForm, 'bed_id': bed_id, 'msg': '荣华养老院客户基本信息'})


@login_required
def adddrughistory(request, bed_id):
    form = EX_RonghuaForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        # cur_bed = get_object_or_404(RonghuaBed, bed_ID=bed_id)
        newEX_Ronghua = EX_Ronghua.objects.create(
            bed_number=bed_id,
            subject_id=form.cleaned_data['subject_id'],
            dose=form.cleaned_data['dose'],
            unit=form.cleaned_data['unit'],
            doctor_advice=form.cleaned_data['doctor_advice'],
            date=form.cleaned_data['date'],
        )
        newEX_Ronghua.save()
        redirect_url = reverse('bedAddDetailsRonghua', args=[bed_id, ])
        return HttpResponseRedirect(redirect_url)
    else:
        newForm = EX_RonghuaForm()
        return render(request, 'add_new_info.html', {'form': newForm, 'bed_id': bed_id, 'msg': '用药记录'})


@login_required
def addnurshistory(request, bed_id):
    form = NU_RonghuaForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        # cur_bed = get_object_or_404(RonghuaBed, bed_ID=bed_id)
        newNU_Ronghua = NU_Ronghua.objects.create(
            bed_number=bed_id,
            subject_id=form.cleaned_data['subject_id'],
            category=form.cleaned_data['category'],
            result=form.cleaned_data['result'],
            date=form.cleaned_data['date'],
        )
        newNU_Ronghua.save()
        redirect_url = reverse('bedAddDetailsRonghua', args=[bed_id, ])
        return HttpResponseRedirect(redirect_url)
    else:
        newForm = NU_RonghuaForm()
        return render(request, 'add_new_info.html', {'form': newForm, 'bed_id': bed_id, 'msg': '护理记录'})


@login_required
def addtemperature(request, bed_id):
    form = PE_RonghuaForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        # cur_bed = get_object_or_404(RonghuaBed, bed_ID=bed_id)
        newPE_Ronghua = PE_Ronghua.objects.create(
            bed_number=bed_id,
            subject_id=form.cleaned_data['subject_id'],
            is_operated=form.cleaned_data['is_operated'],
            category=form.cleaned_data['category'],
            result=form.cleaned_data['result'],
            date=form.cleaned_data['date'],
        )
        newPE_Ronghua.save()
        redirect_url = reverse('bedAddDetailsRonghua', args=[bed_id, ])
        return HttpResponseRedirect(redirect_url)
    else:
        newForm = PE_RonghuaForm()
        return render(request, 'add_new_info.html', {'form': newForm, 'bed_id': bed_id, 'msg': '体温表'})


@login_required
def adddbaby(request, bed_id):
    form = BB_RonghuaForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        # cur_bed = get_object_or_404(RonghuaBed, bed_ID=bed_id)
        newBB_Ronghua = BB_Ronghua.objects.create(
            bed_number=bed_id,
            subject_id=form.cleaned_data['subject_id'],
            category=form.cleaned_data['category'],
            result=form.cleaned_data['result'],
            date=form.cleaned_data['date'],
        )
        newBB_Ronghua.save()
        redirect_url = reverse('bedAddDetailsRonghua', args=[bed_id, ])
        return HttpResponseRedirect(redirect_url)
    else:
        newForm = BB_RonghuaForm()
        return render(request, 'add_new_info.html', {'form': newForm, 'bed_id': bed_id, 'msg': '体温表'})