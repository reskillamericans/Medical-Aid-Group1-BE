from django import urls
from django.urls import path
from django.urls.conf import include
from . import views
from .views import (  
    support_view,
    support_success_view,
    index,
    about_us,
)

urlpatterns = [
    path('', index, name="homepage"),
    path('about-us/', about_us, name = "about-us"),
    path('support/', support_view, name = "support"),
    path('support-success/', support_success_view, name = "support-success"),
    path('faq/', views.faq, name = 'faq'),
    path('contact/', views.CreateContact, name='contact'),
    #path('patient-appt/<int:id>', views.CreateAppointment, name='patient-appt'),
    #path('patient-doctor-profile/<int:id>', views.DocProfile, name='patient-doctor-profile'),
    #path('faq/', views.faq, name = 'faq')

] 
