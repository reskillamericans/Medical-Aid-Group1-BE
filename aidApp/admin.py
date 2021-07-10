from aidApp.models import Appointment, Clinic, Feedback, FAQ, Health_Practitioner, Patient, Pharmacy
from django.contrib import admin
from .models import FAQ

# Register your models here.
<<<<<<< HEAD

admin.site.register(FAQ)
=======
admin.site.register(FAQ)
admin.site.register(Feedback)
admin.site.register(Patient)
admin.site.register(Health_Practitioner)
admin.site.register(Clinic)
admin.site.register(Pharmacy)
admin.site.register(Appointment)
>>>>>>> 76cd49f86edb520f9b45e3e3de5ce1a76ab51f9f
