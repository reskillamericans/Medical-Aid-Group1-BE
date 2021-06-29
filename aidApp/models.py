from django.db import models
from datetime import datetime
import django.utils.datetime_safe

# Create your models here.pyclass Patient(models.Model):

#class Doctors(models.Model):
#    first_name = models.CharField(max_length=50)
#    last_name= models.CharField(max_length=50)
#    email = models.CharField(max_length=50)
#    #clinic = models.CharField(max_length=50)
#    clinic = models.ForeignKey(, null=True, on_delete=models.SET_NULL)
#    pharmacy = models.CharField(max_length=50)

#    def __str__(self) -> str:
#        return self.last_name

class Clinics (models.Model):
    clinic_name = models.CharField(max_length=100)
    open_hours =  models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100, default='0000000', editable=False)

    def __str__(self) -> str:
        return self.clinic_name


class Pharmacies (models.Model):
    pharmacy_name = models.CharField(max_length=100)
    open_hours =  models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.pharmacy_name


class Doctors(models.Model):
    first_name = models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    #clinic = models.CharField(max_length=50)
    clinic = models.ForeignKey(Clinics, null=True, on_delete=models.SET_NULL)
    #pharmacy = models.CharField(max_length=50)
    clinic = models.ForeignKey(Pharmacies, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.last_name

class Patients (models.Model):
    patient_firstName = models.CharField(max_length=100)
    patient_lastName =  models.CharField(max_length=100)
    phone_number = models.IntegerField()
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    #appointments = models.DateTimeField(default= django.utils.datetime_safe.date())
    appointment = models.ForeignKey(Doctors, null=True, on_delete=models.SET_NULL)
    doctor_lastName = models.ForeignKey(Clinics, related_name='doctor_lastNames', null=True, on_delete=models.SET_NULL)
    clinic = models.ForeignKey(Clinics,  related_name='clinics', null=True, on_delete=models.SET_NULL)
    pharmacy = models.ForeignKey(Pharmacies, null=True, on_delete=models.SET_NULL)
    phone_number = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    
    def __str__(self) -> str:
       return self.last_name
class Appointment(models.Model):

    doctors = models.ForeignKey(Doctors, default='0000000', editable=False, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100)
    #date = models.DateTimeField(default= django.utils.datetime_safe.date())
    date = models.DateTimeField(auto_now=True)
    time = models.CharField(max_length=200)
    login = models.CharField(max_length=100, default='0000000', editable=False)

    def __str__(self):
        return '{} {} {}. Patient: {}'.format(self.date, self.time, self.doctors, self.patient_name)
        
class Consultations(models.Model):
    doctor_last_name = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    patient_last_name = models.ForeignKey(Patients, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinics, null=True, on_delete=models.SET_NULL)
    pharmacy = models.ForeignKey(Pharmacies, null=True, on_delete=models.SET_NULL)
    month = models.CharField(max_length=100)
    date = models.IntegerField
    time = models.CharField(max_length=10)

    def __str__(self):
        return self.patient_last_name
class Feedback (models.Model):
    patient_first_name = models.ForeignKey(Patients, default='0000000', editable=False, on_delete = models.CASCADE)
    feedback_or_complaint= models.CharField(max_length=10, default='0000000', editable=False)
    patient_message = models.CharField(max_length=200)
    admin_reply = models.CharField(max_length=200, default='0000000', editable=False)

    def __str__(self) -> str:
        return self.feedback_or_complaint
class FAQ(models.Model):
    question = models.CharField(max_length=400, default='0000000', editable=False)
    answer = models.CharField(max_length=400, default='0000000', editable=False)

    def __str__(self) -> str:
        return self.question







  







