from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from datetime import date
from django.utils import timezone as tz
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail, get_connection
from django.conf import settings
from django.db.models import Q
from .models import Feedback, Patient, Health_Practitioner, FAQ, Appointment, Clinic
from .forms import CreateContactForm#, AppUpdateForm, AppRetrieveForm ,AppCreateForm, DocProfileForm 


# Create your views here.

# Landing page 
def index(request):
    return render(request, 'aidApp/index.html')

# About Us page 
def about_us(request):
    return render(request, 'aidApp/about-us.html')

# FAQ
def faq(request):

    faqs = FAQ.objects.all()
    context = {
        "Faqs":faqs
    }

    return render(request,'aidApp/faq.html',context)

# Contact Us page 

# @login_required
def CreateContact(request):
    
    context = {}
        
    if request.method == 'POST':
         form = CreateContactForm(request.POST)
         if form.is_valid():
             
             subject = form.cleaned_data['subject']
             message = form.cleaned_data['comment']
             sender = form.cleaned_data['email']
             
             administrators = []
             for admin in User.objects.filter(is_superuser=True):
                administrators.append(admin.email)
            
             con = get_connection(settings.EMAIL_BACKEND)
             send_mail(subject,
                      message,
                      sender,
                      administrators,
                      connection=con            
             )
             form.save()
             messages.success(request, "Your message was submitted successfully! Thank you.")
                     
         else:
             
             return render(request,'aidApp/contact/contact.html',{'form': form})
 
    context = {'form': CreateContactForm()}
    return render(request, 'aidApp/contact/contact.html', context) 

