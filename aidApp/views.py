from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import BadHeaderError, send_mail
from .models import Feedback, Patient, Health_Practitioner
import datetime

# Create your views here.
def index(request):
    return HttpResponse("<h1>Medical Aid app Homepage</h1>")

@login_required
def doctor_dash_view(request):
    context = {
        'doctor': Health_Practitioner.objects.all()
    }
    return render(request, 'aidApp/doctor/doctor-dash.html', context)

def doctor_patient_view(request):
    return render(request, 'aidApp/doctor/doctor-patient.html')

def doctor_search_view(request):
    # input and then filter
    patients = Patient.objects.all()

    context = {
        'patients': patients,
        
    }
    return render(request, 'aidApp/doctor/doctor-search.html', context)

def doctor_appointment_view(request):
    return render(request, 'aidApp/doctor/doctor-appointment.html')

def doctor_schedule_view(request):
    return render(request, 'aidApp/doctor/doctor-schedule.html')
    
def doctor_schedule_week_view(request):
    return render(request, 'aidApp/doctor/doctor-schedule-week.html')

@login_required
def doctor_support_view(request):

    user = request.user.username
    currentuser = User.objects.get(username=user)
    fullname = f"{currentuser.first_name} {currentuser.last_name}" 
    email = currentuser.email
    
    context = {
        'fullname': fullname,
        'email': email,
    }
    
    if request.method == "POST":
        if request.POST.get('fullname') and request.POST.get('message'):
            support = Feedback()
            support.fullname = request.POST.get('fullname')
            support.email = request.POST.get('email')
            support.response_type = request.POST.get('complaint')
            support.message = request.POST.get('message')
            support.save()
            send_mail(
                'Contact Support',
                'Your message has been received.  If needed, someone will follow up with you shortly.  Thank you!',               
                'devops4zuri@gmail.com',
                [email],
                fail_silently=False,
                )
            return redirect('doctor-support-success')
        else: 
            messages.error(request, 'Message section can not be empty.  Submit unsuccessful.')
            return render(request, 'aidApp/doctor/doctor-support.html', context) 
    else:
        return render(request, 'aidApp/doctor/doctor-support.html', context)

def doctor_support_success_view(request):
    return render(request, 'aidApp/doctor/doctor-support-feedback.html')

def doctor_signup_view(request):
    return render(request, 'aidApp/doctor/doctor-signup.html')



@login_required
def support_view(request):

    user = request.user.username
    currentuser = User.objects.get(username=user)
    fullname = f"{currentuser.first_name} {currentuser.last_name}" 
    email = currentuser.email
    
    context = {
        'fullname': fullname,
        'email': email,
    }
    
    if request.method == "POST":
        if request.POST.get('fullname') and request.POST.get('message'):
            support = Feedback()
            support.fullname = request.POST.get('fullname')
            support.email = request.POST.get('email')
            support.response_type = request.POST.get('complaint')
            support.message = request.POST.get('message')
            support.save()
            send_mail(
                'Contact Support',
                'Your message has been received.  If needed, someone will follow up with you shortly.  Thank you!',
                'devops4zuri@gmail.com',
                [email],
                fail_silently=False,
                )
            return redirect('support-success')
        else: 
            messages.error(request, 'Message section can not be empty.  Submit unsuccessful.')
            return render(request, 'aidApp/patient/patient-support.html', context) 
    else:
        return render(request, 'aidApp/patient/patient-support.html', context)

def support_success_view(request):
    return render(request, 'aidApp/patient/patient-support-feedback.html')