from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .models import Contact, Feedback, FAQ

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
def contact(request):

    contacts = Contact.objects.all()
    context = {
        "Contacts":contacts
    }

    return render(request,'aidApp/contact.html',context)
