from aidApp.models import Health_Practitioner, Appointment, Feedback, Contact, FAQ, Patient, Pharmacy ,Clinic  
from django.contrib import admin
from .models import FAQ

admin.site.register(FAQ)
admin.site.register(Contact)
admin.site.register(Feedback)
admin.site.register(Patient)
admin.site.register(Health_Practitioner)
admin.site.register(Clinic)
admin.site.register(Pharmacy)
admin.site.register(Appointment)
