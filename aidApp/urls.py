from django import urls
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('adminpage', views.admin_views, name='admin-dash' )
    
]
