from django.urls import path
from . import views

urlpatterns = [path('feedback/', views.Feedback, name='feedback'),
    
]
