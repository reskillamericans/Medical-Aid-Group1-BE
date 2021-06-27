from django.contrib import admin
from .models import Patient, Health_Practitioner, Appointment, FAQ, Clinics, Pharmacies, Feedback


# Register your models here.
admin.site.register(Patient)
admin.site.register(Health_Practitioner)
admin.site.register(FAQ)
admin.site.register(Clinics)
admin.site.register(Pharmacies)
admin.site.register(Feedback)
admin.site.register(Appointment)
