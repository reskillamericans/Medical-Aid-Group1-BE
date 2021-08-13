from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .models import Feedback, FAQ

# Create your views here.

# Landing page 
def index(request):
    return render(request, 'aidApp/index.html')

# About Us page 
def about_us(request):
    return render(request, 'aidApp/about-us.html')

def faq(request):

    faqs = FAQ.objects.all()
    context = {
        "Faqs":faqs

    }
    return render(request,'aidApp/faq.html',context)

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
