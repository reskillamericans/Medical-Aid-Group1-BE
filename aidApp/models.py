from django.db import models
from datetime import date, time
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, SET, SET_NULL
from django.db.models.fields.related import ForeignKey, OneToOneField
from django.forms import widgets


class FAQ(models.Model):

    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question


class Contact(models.Model):

    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    your_email = models.EmailField(max_length=60)
    nature_of_enquiry = models.TextField(default='Feedback', choices=(('Feedback', 'Feedback'),
                                                                       ('Careers', 'Careers'),
                                                                       ('Support', 'Support')))
    subject = models.CharField(max_length=50, null=True)
    your_message = models.TextField(max_length=400)

    def __str__(self):
        return self.subject
    


class Patient(models.Model):
    
    patient = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=20)
    D_O_B = models.DateField(default=date.today())
    registration_date = models.DateTimeField(auto_now_add=True) 
    medical_history = models.TextField(blank=True, null=True)
                
    def __str__(self):
        return self.patient.get_full_name() 


class Health_Practitioner(models.Model):

    health_practitioner = models.OneToOneField(User, on_delete=models.CASCADE)
    professional_title = models.CharField(default= "Dr. ", max_length=50)
    image = models.ImageField(null=True, blank=True) #default='image.jpg', upload_to='profile_pics') 
    telephone = models.CharField(max_length=20)
    specialty = models.TextField(max_length=254)
    consultation_times = models.TextField(default="Monday - 10:00am to 11:00am", max_length=400)
    clinics = models.ManyToManyField('Clinic')
    appointments_pending = models.IntegerField(default=0)
    appointments_approved = models.IntegerField(default=0)

    def __str__(self):
        return self.health_practitioner.get_full_name()
    

class Feedback(models.Model):

    patient = models.ForeignKey(Patient, null=True, on_delete=SET_NULL)
    response_type = models.TextField(default='complaint',choices=(('complaint', 'complaint'), ('other', 'other')))
    subject = models.CharField(max_length=100)
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
    app_date = models.DateField(default=date.today())
    app_time = models.TimeField(default=time(hour=9, minute=00))
    app_status = models.CharField(blank=True, max_length=10)
    

    def __str__(self):
        return "Patient {} Date {} Time {} for {}".format(self.patient, self.app_date, self.app_time, self.health_practitioner)
    
