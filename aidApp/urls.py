from aidApp.views2 import UpdateAppointment
from django import urls
from django.urls import path
from aidApp import views
from django.urls.conf import include

urlpatterns = [

    path('', views.index, name='index'),
    path('contact/', views.CreateContact, name='contact'),

       
]

'''
    path('app_create/', views.CreateAppointment, name='app_create'),
    path('app_retrieve/<int:pk>', views.RetrieveAppointment, name='app_retrieve'),
    path('app_update/<int:pk>', views.UpdateAppointment, name='app_update'),
    path('doc_retrieve/<int:pk>', views.DocProfile, name='doc_retrieve'),
'''