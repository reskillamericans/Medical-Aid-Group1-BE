from django import urls
from django.urls import path
from .views import (
    doctor_dash_view, 
    doctor_profile_view,
    doctor_patient_view, 
    doctor_search_view, 
    doctor_appointment_view, 
    doctor_schedule_view,
    doctor_schedule_week_view,
    doctor_support_view,
    doctor_support_success_view,
    doctor_consultation_view,
    doctor_confirm_view,
    doctor_edit_view,

)

app_name = 'doctor'

urlpatterns = [
    path('doctor-dash/', doctor_dash_view, name = "doctor-dash"),
    path('doctor-patient/', doctor_patient_view, name = "doctor-patient"),
    path('doctor-search/', doctor_search_view, name = "doctor-search"),
    path('doctor-consultations/', doctor_consultation_view, name = "doctor-consultations"),
    path('doctor-appointment/', doctor_appointment_view, name = "doctor-appointment"),
    path('doctor-schedule/', doctor_schedule_view, name = 'doctor-schedule'),
    path('doctor-schedule-week/', doctor_schedule_week_view, name = "schedule-week"),
    path('doctor-support/', doctor_support_view, name = "doctor-support"),
    path('doctor-support-success/', doctor_support_success_view, name = "doctor-support-success"),
    path('doctor-profile/', doctor_profile_view, name = "doctor-profile"),
    path('doctor-confirm/', doctor_confirm_view, name = "doctor-confirm"),
    path('doctor-edit/', doctor_edit_view, name = "doctor-edit"),
        
]
