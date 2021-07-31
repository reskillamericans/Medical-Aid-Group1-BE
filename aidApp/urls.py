from django import urls
from django.urls import path
from django.urls.conf import include
from .views import (
    doctor_dash_view, 
    doctor_patient_view, 
    doctor_search_view, 
    doctor_appointment_view, 
    support_view,
    support_success_view,
    doctor_schedule_view,
    doctor_schedule_week_view,
    doctor_support_view,
    doctor_support_success_view,
)

urlpatterns = [
    path('doctor-dash/', doctor_dash_view, name = "doctor-dash"),
    path('doctor-patient/', doctor_patient_view, name = "doctor-patient"),
    path('doctor-search/', doctor_search_view, name = "doctor-search"),
    path('doctor-appointment/', doctor_appointment_view, name = "doctor-appointment"),
    path('doctor-schedule/', doctor_schedule_view, name = 'doctor-schedule'),
    path('doctor-schedule-week/', doctor_schedule_week_view, name = "schedule-week"),
    path('doctor-support/', doctor_support_view, name = "doctor-support"),
    path('doctor-support-success/', doctor_support_success_view, name = "doctor-support-success"),
    path('support/', support_view, name = "support"),
    path('support-success/', support_success_view, name = "support-success"),
    
    
]

