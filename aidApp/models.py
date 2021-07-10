from datetime import datetime
from django.db import models
from django.urls import reverse


# Create your models here.

class FAQ(models.Model):
    question = models.CharField(max_length=400)
    answer = models.CharField(max_length=400)
    createdby = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.question
