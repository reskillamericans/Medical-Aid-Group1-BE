from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>Medical Aid app Homepage</h1>")

# User Registration (Signup)

def signup(request):

    if request.method == 'POST':
        fullname = request.POST['fullname']
        username= request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1'] 
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(email = email).exists():
                messages.info(request,'Please note that this email is already taken.')
                return render(request,'users/signup.html')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.fullname = fullname
                user.save()
                print('Please note that the user is created.')
                return render(request,'users/login.html')

        else:
            messages.info(request,'Please note that the passwords are not matching.')
            return render(request,'users/signup.html')
        return redirect('/')
    
    else:
        return render(request,'users/signup.html')

# User Login

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = auth.authenticate(email=email, password=password)
            auth.login(request, user)
            return render(request,'/')
        except:
            return render(request,'users/login.html')
    else: 
        return render(request,'users/login.html')

# User Logout

def logout(request):
    try:
        logout(request)
        messages.add_message(request, messages.INFO, 'You are currently logged out.')
    except:
        messages.add_message(request, messages.ERROR, 'You are unable to logout.')
    return render(request,'users/login.html')