from django.db import models
from datetime import date, time
from django.db.models.fields import TextField
from django.utils import timezone as tz
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, SET, SET_NULL
from django.db.models.fields.related import ForeignKey, ManyToManyField, OneToOneField
from django.forms import widgets




class FAQ(models.Model):

    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question


class Contact(models.Model):

    CHOICES = [(None, "Nature of Inquiry"),('feedback','Feedback'),('career','Career'),('support','Support'),]

    fname = models.CharField(max_length=50, null=True)
    lname = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=60, null=True)
    inquiry = models.CharField(choices=CHOICES, max_length=8)
    subject = models.CharField(max_length=50, null=True)
    comment = models.TextField(max_length=400, null=True)

    def __str__(self):
        return self.subject
    

class Patient(models.Model):
    
    patient = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=20)
    sex = models.CharField(default= 'Male', max_length= 20)
    ethnicity = models.CharField(blank=True, null=True, max_length= 90)
    marital_status = models.CharField(default = 'Single', max_length=30)
    D_O_B = models.DateField(default=tz.now)
    registration_date = models.DateTimeField(auto_now_add=True) 
                    
    def __str__(self):
        return self.patient.get_full_name() 


class Medical_History(models.Model):

    #permissions = (('can_edit_medical_history', 'Can update medical history'),)
    
    patient = models.ForeignKey('Patient', null=True, on_delete=models.CASCADE)
    health_practitioner = models.ForeignKey('Health_Practitioner', null=True, on_delete=models.SET_NULL)
    date_visited = models.DateField(default=tz.now)
    patient_concerns = TextField(blank=True, null=True)
    heart_rate = models.IntegerField(blank=True, null=True)
    bP_systolic = models.IntegerField(blank=True, null=True)
    bP_diastolic = models.IntegerField(blank=True, null=True)
    spO2 = models.IntegerField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    bmi = models.FloatField(blank=True, null=True)
    prescriptions = models.TextField(blank=True, null=True)
    test_results = models.TextField(blank=True, null=True)
    health_practitioner_comments = models.TextField(blank=True, null=True)



class Health_Practitioner(models.Model):

    health_practitioner = models.OneToOneField(User, on_delete=models.CASCADE)
    professional_title = models.CharField(default= "Dr. ", max_length=50)
    image = models.ImageField(null=True, blank=True)  
    telephone = models.CharField(max_length=20)
    specialty = models.TextField(max_length=254)
    consultation_times = models.TextField(default="Monday - 10:00am to 11:00am", max_length=600)
    clinics = models.ManyToManyField('Clinic')
    insurance_accepted = models.CharField(default='Blue Cross', max_length=200)
    languages = models.CharField(default='English', max_length=300)
    accepting_new_patients = models.BooleanField(default='True', max_length=5)
    appointments_pending = models.IntegerField(default=0)
    appointments_approved = models.IntegerField(default=0)

    def __str__(self):
        return self.health_practitioner.get_full_name()
    

class Feedback(models.Model):

    CHOICES2 = [('Complaint', 'Complaint'), ('Other', 'Other'),]

    patient = models.ForeignKey(Patient, null=True, on_delete=SET_NULL)
    response_type = models.CharField(max_length=9,choices=CHOICES2)
    message = models.TextField(max_length=400)

    def __str__(self):
        return self.subject


class Pharmacy(models.Model):

    name = models.CharField(max_length=100)
    service_options = models.CharField(max_length=50)
    located_in = models.TextField(max_length=254)
    address = models.TextField(max_length=254)
    hours = models.TextField(max_length=254)
    telephone = models.CharField(max_length=20)
    website = models.URLField(max_length=100)
    directions = models.TextField(max_length=254)
    

    def __str__(self):
        return self.name


class Clinic(models.Model):

    name = models.CharField(max_length=40)
    website = models.URLField(max_length=100)
    located_in = models.TextField(max_length=100)
    address = models.TextField(max_length=254)
    hours = models.TextField(max_length=254) 
    appointments_url = models.URLField(max_length=100)
    telephone = models.CharField(max_length=20)
    question_answer = models.TextField(max_length=254)
    
    def __str__(self):
        return self.name


class Appointment(models.Model):

    class Meta:
        unique_together = ('health_practitioner','app_date', 'app_time') 
        #permissions = (('can_edit_appointment', 'Can update appointment'),)
       
    health_practitioner = models.ForeignKey(Health_Practitioner, null=True, on_delete=models.CASCADE) 
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    app_date = models.DateField(default=tz.now)
    app_time = models.TimeField(default=time(hour=9, minute=00))
    purpose_of_visit = TextField(default= 'Annual Physical Examination', max_length=250)
    app_status = models.CharField(blank=True, max_length=10)
    
    

    def __str__(self):
        return "Patient {} Date {} Time {} for {}".format(self.patient, self.app_date, self.app_time, self.health_practitioner)
    
