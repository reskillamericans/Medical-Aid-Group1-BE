from aidApp.models import Appointment, Clinic, Feedback, FAQ, Health_Practitioner, Patient, Pharmacy
from django.contrib import admin

# Register your models here.
admin.site.register(FAQ)
admin.site.register(Feedback)
admin.site.register(Patient)
admin.site.register(Health_Practitioner)
admin.site.register(Clinic)
admin.site.register(Pharmacy)
admin.site.register(Appointment)
