from django import urls
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [

    path('', views.index, name="homepage"),
    path('about-us/', views.about_us, name = "about-us"),
    path('faq/', views.faq, name = 'faq'),
    path('contact/', views.CreateContact, name='contact'),
    #path('patient-appt/<int:id>', views.CreateAppointment, name='patient-appt'),
    #path('patient-doctor-profile/<int:id>', views.DocProfile, name='patient-doctor-profile'),
    #path('faq/', views.faq, name = 'faq')
  ]
