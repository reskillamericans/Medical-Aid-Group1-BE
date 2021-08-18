from django.db import models
from django.utils import timezone as tz
from django.contrib.auth.models import User
from django.db.models.fields import TextField
from django.db.models.deletion import CASCADE, SET, SET_NULL
from django.db.models.fields.related import ForeignKey, OneToOneField
from django.forms import widgets
import datetime
from phone_field import PhoneField

class FAQ(models.Model):

    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question


class Contact(models.Model):

    CHOICES = [(None, "Nature of Inquiry"),('Feedback','Feedback'),('Career','Career'),('Support','Support'),]

    fname = models.CharField(max_length=50, null=True)
    lname = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=60, null=True)
    inquiry = models.CharField(choices=CHOICES, default= "Feedback", max_length=8)
    subject = models.CharField(max_length=50, null=True)
    comment = models.TextField(max_length=400, null=True)

    def __str__(self):
        return self.subject



class Patient(models.Model):
    
    patient = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = PhoneField(blank=True, help_text='Patient phone number')
    D_O_B = models.DateField(default=tz.now)
    # age = models.CharField(max_length=5)
    registration_date = models.DateTimeField(auto_now_add=True)
    sex = models.CharField(max_length=20)
    marital_status = models.CharField(max_length=50) 
    # medical_history = models.TextField(blank=True, null=True)
    @property
    def age(self):
        return tz.now().year - self.D_O_B.year
    
    def __str__(self):
        return self.patient.get_full_name() 


'''class Medical_History(models.Model):

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
'''

class Health_Practitioner(models.Model):

    health_practitioner = models.OneToOneField(User, on_delete=models.CASCADE)
    professional_title = models.CharField(default= "Dr. ", max_length=4)
    professional_suffix = models.CharField(default= " MD", max_length=4)
    #image = models.ImageField(null=True, blank=True)  
    telephone = models.CharField(max_length=20)
    specialty = models.TextField(max_length=200)
    consultation_times = models.TextField(default="Monday - 10:00am to 11:00am", max_length=600)
    clinics = models.ForeignKey('Clinic', on_delete=models.CASCADE)
    insurance_accepted = models.CharField(default='Blue Cross', max_length=200)
    languages = models.CharField(default='English', max_length=60)
    accepting_new_patients = models.CharField(default='Yes', max_length=3)
    reviews = models.IntegerField(default=29)
    rating_reviews = models.FloatField(default=4.7)
    patient_comments = models.IntegerField(default=25)
    appointments_pending = models.IntegerField(default=0)
    appointments_approved = models.IntegerField(default=0)

    def __str__(self):
        return self.health_practitioner.get_full_name()
    

class Feedback(models.Model):

    # patient = models.ForeignKey(Patient, null=True, on_delete=SET_NULL)
    fullname = models.CharField(max_length=200)
    email = models.EmailField(max_length=60)
    response_type = models.CharField(max_length=50)
    # response_type = models.TextField(default='complaint',choices=(('complaint', 'complaint'), ('other', 'other')))
    # subject = models.CharField(max_length=100)
    message = models.TextField(max_length=400)

    def __str__(self):
        return self.fullname


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
    availability = models.TextField(default="Monday, Tuesday", max_length=60)

    #consultation times - specific to each Clinic
    
    def __str__(self):
        return self.name
    

class Appointment(models.Model):

    DAYS = [(day, day) for day in range(1, 32)]
    MONTHS = [(month, month) for month in range(1, 13)]
    YEARS = [(year, year) for year in [2021, 2022, 2023, 2024]]
    TIMESLOTS = [(0, '9:00 AM'),
                (1, '10:00 AM'),
                (2, '11:00 AM'),
                (3, '12:00 PM'),
                (4, '1:00 PM'),
                (5, '2:00 PM'),
                (6, '3:00 PM'),
                (7, '4:00 PM'),
                (8, '5:00 PM')]
    
    
    health_practitioner = models.ForeignKey(Health_Practitioner, null=True, on_delete=models.CASCADE) 
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    app_date_day = models.IntegerField(choices=DAYS, default=1)
    app_date_month = models.IntegerField(choices=MONTHS, default=1)
    app_date_year = models.IntegerField(choices=YEARS, default=2021)
    timeslots = models.IntegerField(choices=TIMESLOTS, default=0)
    appt_reason = TextField(default= 'Annual Physical Examination', max_length=200)
    app_status = models.CharField(blank=True, max_length=10)
  
    def __str__(self):
        return "Patient {} Date {} Time {} for {}".format(self.patient, self.app_date, self.time, self.health_practitioner)
    
    @property
    def time(self):
        return self.TIMESLOTS[self.timeslots][1]

    @property
    def app_date(self): 
        y = self.YEARS[self.app_date_year][1]
        m = self.MONTHS[self.app_date_month][1]
        d = self.DAYS[self.app_date_day][1]
        
        return '{}-{}-{}'.format(y, m, d) 
