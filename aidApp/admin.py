from django.contrib import admin
#from .models import Doctors, Clinics, Pharmacies, Patients,Appointment, Consultations, Feedback, FAQ
from .models import Doctors, Clinics, Pharmacies, Patients,Consultations, Feedback, FAQ


# Register your models here.
admin.site.register(Doctors)
admin.site.register(Clinics)
admin.site.register(Pharmacies)
admin.site.register(Patients)
#admin.site.register(Appointment)
admin.site.register(Consultations)
admin.site.register(Feedback)
admin.site.register(FAQ)