from django import forms
from django.forms import ModelForm
from .models.ronghua_models import *
from .models.yiyuan_models import *


class BedForm(forms.Form):
    bed_ID = forms.IntegerField(label='床号')


class PatientForm(ModelForm):

    class Meta:
        model = Patient
        widgets = {
            # 'in_date': DateTimePicker(options={"format": "YYYY-MM-DD HH:mm", "pickSeconds": False}),
            # 'out_date': DateTimePicker(options={"format": "YYYY-MM-DD HH:mm", "pickSeconds": False})
            'in_date': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
            'out_date': forms.DateTimeInput(attrs={'class': 'datetime-input'})
        }
        exclude = ['bed_number']


class PatientMHForm(ModelForm):
    # inquiry_date = forms.DateField(label="问诊时间", widget=forms.DateInput(attrs={'type': 'date'}), required=False)

    class Meta:
        model = PatientMH
        widgets = {'past_history': forms.TextInput(attrs={'style':'height:30px; width: 700px'}),
                   'personal_history': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),
                   'family_history': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),
                   'in_symptom': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),
                   'out_symptom': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),
                   'inquiry_date': forms.DateInput(attrs={'type': 'date'})}
        exclude = ['bed_number']


class PatientTEForm(ModelForm):
    # date = forms.DateField(label="问诊时间", widget=forms.DateInput(attrs={'type': 'date'}), required=False)

    class Meta:
        model = PatientTE
        widgets = {'exam_program': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),
                   'result': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),
                   'all_result': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),
                   'date': forms.DateInput(attrs={'type': 'date'})}
        exclude = ['bed_number']


class PatientLBForm(ModelForm):
    # date = forms.DateField(label="检验时间", widget=forms.DateInput(attrs={'type': 'date'}), required=False)

    class Meta:
        model = PatientLB
        widgets = {'category': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),
                   'subcategory': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),
                   'exam_program': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),
                   'result': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),
                   'date': forms.DateInput(attrs={'type': 'date'})}
        exclude = ['bed_number']


class PatientEXForm(ModelForm):
    # date = forms.DateField(label="给药日期", widget=forms.DateInput(attrs={'type': 'date'}), required=False)

    class Meta:
        model = PatientEX
        widgets = {'dose': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),
                   'date': forms.DateInput(attrs={'type': 'date'})}
        exclude = ['bed_number']


class PatientPRForm(ModelForm):
    # date = forms.DateField(label="手术时间", widget=forms.DateInput(attrs={'type': 'date'}), required=False)

    class Meta:
        model = PatientPR
        widgets = {'date': forms.DateInput(attrs={'type': 'date'})}
        exclude = ['bed_number']


class PatientPEForm(ModelForm):
    # date = forms.DateField(label="体格检查日期", widget=forms.DateInput(attrs={'type': 'date'}), required=False)

    class Meta:
        model = PatientPE
        widgets = {'result': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),
                   'date': forms.DateInput(attrs={'type': 'date'})}
        exclude = ['bed_number']


class DM_RonghuaForm(ModelForm):
    # in_date = forms.DateField(label="入院日期", widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    # out_date = forms.DateField(label="出院日期", widget=forms.DateInput(attrs={'type': 'date'}), required=False)

    class Meta:
        model = DM_Ronghua
        widgets = {'in_diagnose': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),
                   'in_date': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
                   'out_date': forms.DateTimeInput(attrs={'class': 'datetime-input'})}
        exclude = ['bed_number']


class EX_RonghuaForm(ModelForm):
    # date = forms.DateField(label="给药日期", widget=forms.DateInput(attrs={'type': 'date'}), required=False)

    class Meta:
        model = EX_Ronghua
        widgets = {'date': forms.DateInput(attrs={'type': 'date'})}
        exclude = ['bed_number']


class NU_RonghuaForm(ModelForm):
    # date = forms.DateField(label="护理时间", widget=forms.DateInput(attrs={'type': 'date'}), required=False)

    class Meta:
        model = NU_Ronghua
        widgets = {'result': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),
                   'date': forms.DateInput(attrs={'type': 'date'})}
        exclude = ['bed_number']


class PE_RonghuaForm(ModelForm):
    # date = forms.DateField(label="检验时间", widget=forms.DateInput(attrs={'type': 'date'}), required=False)

    class Meta:
        model = PE_Ronghua
        widgets = {'result': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),
                   'date': forms.DateInput(attrs={'type': 'date'})}
        exclude = ['bed_number']


class BB_RonghuaForm(ModelForm):
    # date = forms.DateField(label="检验时间", widget=forms.DateInput(attrs={'type': 'date'}), required=False)

    class Meta:
        model = BB_Ronghua
        widgets = {'result': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),
                   'date': forms.DateInput(attrs={'type': 'date'})}
        exclude = ['bed_number']

