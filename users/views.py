from django.shortcuts import render, redirect
from users.forms import Patient_SignUpForm, Doctor_SignUpForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

# Create your views here.

# Index 

def index(request):
    return HttpResponse("<h1>Medical Aid app Homepage</h1>")

# Patient's Dashboard

def patient_dashboard(request):
    return render(request,'users/patient-dash.html')

# Doctor's Dashboard

def doctor_dashboard(request):
    return render(request,'users/doctor-dash.html')

# Patient User Registration (Signup)

def patient_signup(request):
    if request.method == 'POST':
        form = Patient_SignUpForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            print('Please note that the user is created.')
            
            # Load the profile instance created by the signal
            user.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
 
            # Login user after signing up
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('users:login')

            # Redirect user to patient's dashboard
        return redirect('users:patient-dash')

    else:
        form = Patient_SignUpForm()
        
    args = {'form': form}
    return render(request,'users/signup.html', args)

# Doctor User Registration (Doctor-Signup)

def doctor_signup(request):
    if request.method == 'POST':
        form = Doctor_SignUpForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            print('Please note that the user is created.')
            
            # Load the profile instance created by the signal
            user.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
 
            # Login user after signing up
            user = authenticate(request, username=username, password=password)
            login(request, user)
        
            # Redirect user to doctor's dashboard
        return redirect('users:doctor-dash')

    else:
        form = Doctor_SignUpForm()
        
    args = {'form': form}
    return render(request,'users/doctor-signup.html', args)

# User Login

def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username', 'default')
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return render(request,'users/index.html')
        
        else:
            context["error"] = "Please provide valid credentials."
            return render(request,'users/login.html')
    else: 
        return render(request,'users/login.html', context)