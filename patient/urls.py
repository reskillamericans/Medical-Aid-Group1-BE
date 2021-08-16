from django import urls
from django.urls import path
from .views import (
    support_view,
    support_success_view,
    patient_dash_view,
    patient_doctor_view
)


urlpatterns = [
    path('support/', support_view, name = "support"),
    path('support-success/', support_success_view, name = "support-success"),
    path('patient-dash/', patient_dash_view, name = "patient-dash"),
    path('patient-doctor/', patient_doctor_view, name = "patient-doctor"),
        
]