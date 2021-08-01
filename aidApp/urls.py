from aidApp.views import CreateContact
from django import urls
from django.urls import path
from aidApp import views
from django.urls.conf import include

urlpatterns = [

    path('', views.index, name='index'),
    path('contact/', views.CreateContact, name='contact'),
     
]