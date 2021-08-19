from aidApp.models import Health_Practitioner, Patient
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

# Create your views here.

# Patient's Dashboard

def patient_dash_view(request):
    return render(request,'patient/patient-dash.html')

# Doctor's Dashboard

def doctor_dash_view(request):
    return render(request,'doctor/doctor-dash.html')

# User Registration (Signup)

def patient_signup(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1') 
        password2 = request.POST.get('password2')
        
        if password1==password2:
            if User.objects.filter(email=email).first():
                messages.info(request, 'Please note that this email is already taken.')
                return redirect('users:signup')

            else:
                user = User(username=email, email=email, first_name=first_name, last_name=last_name)
                user.set_password(password1)
                user.save()
                patient = Patient.objects.create(patient=user)
                patient.save()
                messages.info(request,'Please note that the user is created.')
                # Login user after signing up
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                # Redirect to patient's dashboard
                return redirect('patient:patient-dash')

        else:
            messages.info(request,'Please note invalid credentials.')
    else:
        
        return render(request,'users/signup.html') 

# Doctor User Registration (Doctor-Signup)

def doctor_signup(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1') 
        password2 = request.POST.get('password2')
        
        if password1==password2:
            if User.objects.filter(email=email).first():
                messages.info(request,'Please note that this email is already taken.')
                return redirect('users:doctor-signup')

            else:
                user = User(username=email, email=email, first_name=first_name, last_name=last_name)
                user.set_password(password1)
                user.save()
               
                #doctor=Health_Practitioner.objects.create(Health_Practitioner=user)
                #doctor.save()
                
                messages.info(request,'Please note that the user is created.')
                # Login user after signing up
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                
                # Redirect to doctor's dashboard
                return redirect('doctor:doctor-dash')

        else:
            messages.info(request,'Please note invalid credentials.')
    else:
        
        return render(request,'users/doctor-signup.html') 

            
            
# User Login 

def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password1')
        print(username,password)
        # Authenticate user
        user = authenticate(request, username=username,password=password)
        print(user)
        # Verify user is valid
        if user is not None:
            login(request, user)
            patient = Patient.objects.filter(patient=user)
            
            if patient is not None:
                login(request, user)
                return redirect('patient:patient-dash')
            else:
                login(request, user)
                return redirect('doctor:doctor-dash')
        
        else:
            context["error"] = "Please provide valid credentials."
            return render(request,'users/login.html')  

    else: 
        
        return render(request,'users/login.html')
       

# User Logout

def logout_view(request):
    try:
        logout(request)
        messages.add_message(request, messages.INFO, 'You are currently logged out.')
    except:
        messages.add_message(request, messages.ERROR, 'You are unable to logout.')
    return render(request,'users/login.html')