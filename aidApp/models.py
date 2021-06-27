from django.db import models
from datetime import datetime

# Create your models here.pyclass Patient(models.Model):
class Patient (models.Model):
    FirstName = models.CharField(max_length=100)
    LastName =  models.CharField(max_length=100)
    Phonenumber = models.IntegerField()
    Email = models.CharField(max_length=100)
    Password = models.CharField(max_length=200)
    Appointments = models.DateTimeField(auto_now=True)
    Login = models.CharField(max_length=100, default='0000000', editable=False)

    
    def __str__(self) -> str:
       return self.FirstName

class Health_Practitioner (models.Model):
    Patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
    FirstName = models.CharField(max_length=100)
    LastName =  models.CharField(max_length=100)
    Phonenumber = models.IntegerField()
    Email = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    AssistanceTimeReady = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.Patient

class Appointment(models.Model):

    health_practitioner = models.ForeignKey(Health_Practitioner, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.CharField(max_length=100)

    def __str__(self):
        return '{} {} {}. Patient: {}'.format(self.date, self.time, self.health_practitioner, self.patient_name)
        
class FAQ (models.Model):
    Yes =  models.CharField(max_length=100)
    No =  models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.Yes

class Clinics (models.Model):
    ManageProfile = models.ForeignKey(Health_Practitioner, on_delete = models.CASCADE)
    ViewConsultations =  models.CharField(max_length=100)
    ViewPatients = models.CharField(max_length=100)
    SeeScheduledConsultations = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.ManageProfile

class Pharmacies (models.Model):
    ManageProfile = models.ForeignKey(Health_Practitioner, on_delete = models.CASCADE)
    ViewConsultations =  models.CharField(max_length=100)
    ViewPatients = models.CharField(max_length=100)
    SeeScheduledConsultations = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.ManageProfile

class Feedback (models.Model):
    ViewFeedback = models.ForeignKey(Health_Practitioner, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return self.ViewFeedback





  







