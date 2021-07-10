from aidApp.models import Appointment, Clinic, Feedback, FAQ, Health_Practitioner, Patient, Pharmacy
from django.contrib import admin
from .models import FAQ

# Register your models here.
<<<<<<< HEAD

admin.site.register(FAQ)
=======
>>>>>>> 871c78bcc9e1369f8e334ea721a15063db51603b
admin.site.register(FAQ)
admin.site.register(Feedback)
admin.site.register(Patient)
admin.site.register(Health_Practitioner)
admin.site.register(Clinic)
admin.site.register(Pharmacy)
admin.site.register(Appointment)
