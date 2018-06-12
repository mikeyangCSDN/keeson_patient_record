from django.contrib import admin

# Register your models here.
from .models import *


class PatientBedAdmin(admin.ModelAdmin):
    list_display = ['bed_ID', 'device_id', 'date']
    search_fields = ['bed_ID']


class PatientAdmin(admin.ModelAdmin):
    list_display = ['bed_number', 'subject_id', 'gender', 'in_date', 'out_date']
    list_filter = ['bed_number']
    search_fields = ['bed_number']


class PatientMHAdmin(admin.ModelAdmin):
    list_display = ['bed_number', 'subject_id', 'inquiry_date']
    list_filter = ['bed_number']
    search_fields = ['bed_number']


class PatientTEAdmin(admin.ModelAdmin):
    list_display = ['bed_number', 'subject_id', 'date']
    list_filter = ['bed_number', 'date']
    search_fields = ['bed_number']


class PatientLBAdmin(admin.ModelAdmin):
    list_display = ['bed_number', 'subject_id', 'date']
    list_filter = ['bed_number', 'date']
    search_fields = ['bed_number']


class PatientEXAdmin(admin.ModelAdmin):
    list_display = ['bed_number', 'subject_id', 'date']
    list_filter = ['bed_number', 'date']
    search_fields = ['bed_number']


class PatientPRAdmin(admin.ModelAdmin):
    list_display = ['bed_number', 'subject_id', 'date']
    list_filter = ['bed_number', 'date']
    search_fields = ['bed_number']


class PatientPEAdmin(admin.ModelAdmin):
    list_display = ['bed_number', 'subject_id', 'date']
    list_filter = ['bed_number', 'date']
    search_fields = ['bed_number']


admin.site.register(PatientBed, PatientBedAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(PatientMH, PatientMHAdmin)
admin.site.register(PatientTE, PatientTEAdmin)
admin.site.register(PatientLB, PatientLBAdmin)
admin.site.register(PatientEX, PatientEXAdmin)
admin.site.register(PatientPR, PatientPRAdmin)
admin.site.register(PatientPE, PatientPEAdmin)


class RonghuaBedAdmin(admin.ModelAdmin):
    search_fields = ['bed_ID']


class DM_RonghuaAdmin(admin.ModelAdmin):
    list_display = ['bed_number', 'subject_id', 'gender', 'in_date', 'out_date']
    list_filter = ['bed_number']
    search_fields = ['bed_number']


class EX_RonghuaAdmin(admin.ModelAdmin):
    list_display = ['bed_number', 'subject_id', 'date']
    list_filter = ['bed_number', 'date']
    search_fields = ['bed_number']


class NU_RonghuaAdmin(admin.ModelAdmin):
    list_display = ['bed_number', 'subject_id', 'category', 'date']
    list_filter = ['bed_number', 'date']
    search_fields = ['bed_number']


class PE_RonghuaAdmin(admin.ModelAdmin):
    list_display = ['bed_number', 'subject_id', 'category', 'date']
    list_filter = ['bed_number', 'date']
    search_fields = ['bed_number']


class BB_RonghuaAdmin(admin.ModelAdmin):
    list_display = ['bed_number', 'subject_id', 'category', 'date']
    list_filter = ['bed_number', 'date']
    search_fields = ['bed_number']


# admin.site.register(RonghuaBed, RonghuaBedAdmin)
admin.site.register(DM_Ronghua, DM_RonghuaAdmin)
admin.site.register(EX_Ronghua, EX_RonghuaAdmin)
admin.site.register(NU_Ronghua, NU_RonghuaAdmin)
admin.site.register(PE_Ronghua, PE_RonghuaAdmin)
admin.site.register(BB_Ronghua, BB_RonghuaAdmin)
