from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

# Create your views here.

# Patient's Dashboard

def patient_dashboard(request):
    return render(request,'users/patient-dash.html')

# Doctor's Dashboard

def doctor_dashboard(request):
    return render(request,'users/doctor-dash.html')

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
                user_obj = User(username=email, email=email, first_name=first_name, last_name=last_name)
                user_obj.set_password(password1)
                user_obj.save()
                messages.info(request,'Please note that the user is created.')
                # Login user after signing up
                return render(request,'users/login.html')
           # Redirect to patient's dashboard
        return redirect('users:patient-dash')
       
    else:
        messages.info(request,'Please note invalid credentials.')
        
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
                messages.info(request, 'Please note that this email is already taken.')
                return redirect('users:doctor-signup')

            else:
                user_obj = User(username=email, email=email, first_name=first_name, last_name=last_name)
                user_obj.set_password(password1)
                user_obj.save()
                messages.info(request,'Please note that the user is created.')
                # Login user after signing up
                return render(request,'users/login.html')
           # Redirect to doctor's dashboard
        return redirect('users:doctor-dash')
       
    else:
        messages.info(request,'Please note invalid credentials.')
        
    return render(request,'users/doctor-signup.html')
            
            
# User Login 

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password1')
    
        # Authenticate user
        user = authenticate(request, username=username,password=password)

        # Verify user is valid
        if user is not None:
            login(request, user)
            return redirect('users:patient-dashboard')
        else:
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