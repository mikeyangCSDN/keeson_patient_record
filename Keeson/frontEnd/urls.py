from django.urls import path

from frontEnd.view import yiyuan_views
from frontEnd.view import ronghua_views
from frontEnd.view import admin_views

urlpatterns = [
    path('homepage/', admin_views.homepage, name='homepage'),
    path('display_page/', admin_views.displaypage, name='displayPage'),
    path('bed_detail/<str:device_id>/', admin_views.beddetail, name='bedDetail'),

    path('display_test/', admin_views.display_test, name='displayTest'),
    path('display_daily_info/', admin_views.display_daily_info, name='displayDailyInfo'),

    path('bed_add_details/<int:bed_id>/', yiyuan_views.bedadddetails, name='bedAddDetails'),
    path('add_people/<int:bed_id>/', yiyuan_views.addpeople, name='addPerson'),
    path('add_med_history/<int:bed_id>/', yiyuan_views.addmedhistory, name='addMedHis'),
    path('add_day_diag/<int:bed_id>/', yiyuan_views.adddaydiag, name='addDayDiag'),
    path('add_rad_report/<int:bed_id>/', yiyuan_views.addradreport, name='addRadReport'),
    path('add_drug_history/<int:bed_id>/', yiyuan_views.adddrughistory, name='addDrugHistory'),
    path('add_surg_history/<int:bed_id>/', yiyuan_views.addsurghistory, name='addSurgHistory'),
    path('add_body_status/<int:bed_id>/', yiyuan_views.addbodystatus, name='addBodyStatus'),
    path('yiyuan_bed_detail/<int:bed_id>/', yiyuan_views.beddetail, name='yiyuanBedDetail'),
    path('patient_detail/<int:subject_id>/', yiyuan_views.patientdetail, name='yiyuanPatientDetail'),
    path('patient_detail_single/<int:subject_id>/', yiyuan_views.singlePatientDetail, name='yiyuanPatientDetailSingle'),

    path('ronghua_bed_add_details/<str:bed_id>/', ronghua_views.bedadddetails, name='bedAddDetailsRonghua'),
    path('ronghua_add_people/<str:bed_id>/', ronghua_views.addpeople, name='addPersonRonghua'),
    path('ronghua_add_drug_history/<str:bed_id>/', ronghua_views.adddrughistory, name='addDrugHistoryRonghua'),
    path('ronghua_add_nursery_history/<str:bed_id>/', ronghua_views.addnurshistory, name='addNurHistoryRonghua'),
    path('ronghua_add_temperature/<str:bed_id>/', ronghua_views.addtemperature, name='addTempRonghua'),
    path('ronghua_add_baby/<str:bed_id>/', ronghua_views.adddbaby, name='addBabyRonghua'),
]
