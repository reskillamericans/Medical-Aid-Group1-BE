from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Patient, Health_Practitioner

@receiver(post_save, sender=User)
def create_patient_profile(sender, instance, created, **kwargs):
    if created:
        Patient.objects.create(patient=instance)
    instance.patient.save()   

@receiver(post_save, sender=User)
def create_doctor_profile(sender, instance, created, **kwargs):
    if created:
        Health_Practitioner.objects.create(health_practitioner=instance)
    instance.health_practitioner.save()   