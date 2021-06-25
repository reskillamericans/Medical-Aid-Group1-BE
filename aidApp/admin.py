from django.contrib import admin
from .models import Patient, Health_Practitioner, ManageProfile, ViewClinicsPharmInLocation, ViewHealthPractitioners, GiveFeedbackCompliants


# Register your models here.
admin.site.register(Patient)
admin.site.register(Health_Practitioner)
admin.site.register(ManageProfile)
admin.site.register(ViewClinicsPharmInLocation)
admin.site.register(ViewHealthPractitioners)
admin.site.register(GiveFeedbackCompliants)
