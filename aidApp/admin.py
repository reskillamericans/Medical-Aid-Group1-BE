from aidApp.models import Appointment, Feedback, Contact, FAQ, Health_Practitioner, Patient, Pharmacy ,Clinic
from django.contrib import admin
from .models import FAQ

# Register your models here.
admin.site.register(FAQ)
admin.site.register(Contact)
admin.site.register(Feedback)
admin.site.register(Patient)
admin.site.register(Health_Practitioner)
admin.site.register(Clinic)
admin.site.register(Pharmacy)
admin.site.register(Appointment)
