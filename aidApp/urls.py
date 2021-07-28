from django import urls
from django.urls import path
from django.urls.conf import include
from .views import doctor_dash_view, doctor_patient_view, doctor_search_view, doctor_appointment_view

urlpatterns = [
    path('doctor-dash/', doctor_dash_view, name = "doctor-dash"),
    path('doctor-patient/', doctor_patient_view, name = "doctor-patient"),
    path('doctor-search/', doctor_search_view, name = "doctor-search"),
    path('doctor-appointment/', doctor_appointment_view, name = "doctor-appointment"),
    
]
