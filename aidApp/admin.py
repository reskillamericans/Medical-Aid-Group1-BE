from email.headerregistry import Group
from aidApp.models import Health_Practitioner, Appointment, Feedback, Contact, FAQ, Patient, Pharmacy, Clinic  
from django.contrib import admin
from .models import FAQ
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin

# ADMIN PAGE TITLE
admin.site.site_header = 'Medical Aid Admin Dashboard'

# AID APP MODELS, ADMIN MODELS
admin.site.register(FAQ)
admin.site.register(Contact)
admin.site.register(Feedback)
admin.site.register(Appointment)

class Patients_Admin(admin.ModelAdmin):
    list_display = ('__str__', 'D_O_B', 'telephone')

admin.site.register(Patient, Patients_Admin)

class Health_Practioner_Admin(admin.ModelAdmin):
    list_display = ('__str__', 'specialty', 'telephone', 'consultation_times')

admin.site.register(Health_Practitioner, Health_Practioner_Admin)

class Clinic_Admin(admin.ModelAdmin):
    list_display = ('name', 'located_in', 'address', 'telephone', 'website')

admin.site.register(Clinic, Clinic_Admin)

class Pharmacy_Admin(admin.ModelAdmin):
    list_display = ('name', 'service_options', 'located_in', 'address', 'telephone', 'website')

admin.site.register(Pharmacy, Pharmacy_Admin)

# USERS ADMIN
# UserAdmin.list_display = ('first_name', 'last_name', 'email', 'date_joined')#, 'is_active', 'date_joined', 'is_staff') 'groups'

# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
# admin.site.unregister(Group)