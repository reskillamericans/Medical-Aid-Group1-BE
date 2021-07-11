from datetime import datetime
from django.db import models
#from django.db.models.constraints import UniqueConstraint
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, SET, SET_NULL
from django.db.models.fields.related import ForeignKey, OneToOneField


class FAQ(models.Model):

    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question


class Patient(models.Model):
    
    patient = models.ForeignKey(User, on_delete=CASCADE)    
    telephone = models.CharField(max_length=20)
    
    def __str__(self):
        return self.patient.first_name 


class Health_Practitioner(models.Model):

    health_practitioner = models.ForeignKey(User, on_delete=CASCADE)
    telephone = models.CharField(max_length=20)
    specialty = models.TextField(max_length=254)
    #scheduled_appointment = models.TextField(max_length=150, default=None)
    #approved_appointment = models.TextField(max_length=150, default=None)
            
    def __str__(self):
        return self.health_practitioner.first_name


class Feedback(models.Model):

    patient = models.ForeignKey(Patient, null=True, on_delete=SET_NULL)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=254)

    def __str__(self):
        return self.subject


class Pharmacy(models.Model):

    name = models.CharField(max_length=40)
    service_options = models.CharField(max_length=50)
    located_in = models.TextField(max_length=254)
    address = models.TextField(max_length=254)
    hours = models.TextField(max_length=254)
    telephone = models.CharField(max_length=20)
    website = models.URLField(max_length=60)
    directions = models.TextField(max_length=254)
    

    def __str__(self):
        return self.name


class Clinic(models.Model):

    name = models.CharField(max_length=40)
    website = models.TextField(max_length=60)
    located_in = models.TextField(max_length=100)
    address = models.TextField(max_length=254)
    hours = models.TextField(max_length=254) 
    appointments_url = models.URLField(max_length=20)
    telephone = models.CharField(max_length=20)
    question_answer = models.TextField(max_length=254)
    
    def __str__(self):
        return self.name


class Appointment(models.Model):

    class Meta:
       unique_together = ('health_practitioner', 'date_time')

    health_practitioner = models.ForeignKey(Health_Practitioner, on_delete=CASCADE)
    patient = models.ForeignKey(Patient, on_delete=CASCADE)
    date_time = models.DateTimeField()
    is_approved = models.BooleanField(default=False)
    

    def __str__(self):
        return '{} {}. Patient: {}'.format(self.date_time, self.health_practitioner.last_name, self.patient.first_name)