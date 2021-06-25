from django.db import models
from datetime import datetime

# Create your models here.pyclass Patient(models.Model):
class Patient (models.Model):
    FirstName = models.CharField(max_length=100)
    LastName =  models.CharField(max_length=100)
    Phonenumber = models.IntegerField()
    Email = models.CharField(max_length=100)
    Password = models.CharField(max_length=200)
    Appointments = models.DateTimeField(auto_now=True)
    Login = models.CharField(max_length=100, default='0000000', editable=False)

    
    def __str__(self) -> str:
       return self.FirstName

class Health_Practitioner (models.Model):
    Patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
    FirstName = models.CharField(max_length=100)
    LastName =  models.CharField(max_length=100)
    Phonenumber = models.IntegerField()
    Email = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    AssistanceTimeReady = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.FirstName


class ManageProfile(models.Model):
    #LoggedIn = models.ForeignKey(Patient, on_delete = models.CASCADE)
    LoggedIn = models.CharField(max_length=100)
    LoggedResponse = models.CharField(max_length=100)
    Dashboard = models.CharField(max_length=100)
    LogIn = models.CharField(max_length=100)
    MyProfile = models.ForeignKey(Patient, on_delete= models.CASCADE)
    TalkToDoctor = models.ForeignKey(Health_Practitioner, on_delete=models.CASCADE)
    SignUp = models.CharField(max_length=100)
    ProfilePage = models.CharField(max_length=100)
    Finish = models.CharField(max_length=100)

class ViewClinicsPharmInLocation(models.Model):
    #LoggedIn = models.ForeignKey(Patient, on_delete = models.CASCADE)
    LoggedIn = models.CharField(max_length=100)
    LoggedResponse = models.CharField(max_length=100)
    Dashboard = models.CharField(max_length=100)
    LogIn = models.CharField(max_length=100)
    SelectPharmaciesClinics = models.CharField(max_length=100)
    SearchPage = models.CharField(max_length=100)
    SignUp = models.ForeignKey(ManageProfile, on_delete = models.CASCADE)
    GrantLocationPermission = models.CharField(max_length=100)
    SelectPharmacyClinicFromPage = models.CharField(max_length=100)
    DefaultResults = models.CharField(max_length=100)
    SearchByKeyWord = models.CharField(max_length=100)
    SearchedResults = models.CharField(max_length=100)
    ClickOnPharmacyClinic = models.CharField(max_length=100)
    InformationPage = models.CharField(max_length=100)
    Finish = models.CharField(max_length=100)


class ViewHealthPractitioners(models.Model):
     LoggedIn = models.ForeignKey(Patient, on_delete = models.CASCADE)
     LoggedResponse = models.CharField(max_length=100)
     Dashboard = models.CharField(max_length=100)
     LogIn = models.CharField(max_length=100)
     #TalkToDoctor = models.ForeignKey(Health_Practitioner, on_delete=models.CASCADE)
     TalkToDoctor = models.CharField(max_length=100)
     SignUp = models.ForeignKey(ManageProfile, on_delete = models.CASCADE)
     SearchPageDefaultDoctors = models.CharField(max_length=100)
     SearchByKeyWord = models.CharField(max_length=100)
     SearchedResults = models.CharField(max_length=100)
     #ClickOnDoctorsName = models.ForeignKey(Health_Practitioner, on_delete=models.CASCADE)
     ClickOnDoctorsName = models.CharField(max_length=100)
     InformationPage = models.CharField(max_length=100)
     ClickOnScheduleAppointment = models.CharField(max_length=100)
     AvailableTimeModal = models.CharField(max_length=100)
     SelectPreferredTimeAddExtraContinue = models.CharField(max_length=100)
     ConfirmationPage = models.CharField(max_length=100)
     Finish = models.CharField(max_length=100)
     

class GiveFeedbackCompliants(models.Model):
    LoggedIn = models.ForeignKey(Patient, on_delete = models.CASCADE)
    LoggedResponse = models.CharField(max_length=100)
    Dashboard = models.CharField(max_length=100)
    LogIn = models.CharField(max_length=100)
    SignUp = models.CharField(max_length=100)
    ClickOnContactSupport = models.CharField(max_length=100)
    ContactSupportPage = models.CharField(max_length=100)
    EnterNameEmailChooseCategorySend = models.CharField(max_length=100)
    SuccessfulPage = models.CharField(max_length=100)
    Finish = models.CharField(max_length=100)




  







