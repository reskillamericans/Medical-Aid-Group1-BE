from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Medical Aid app Homepage</h1>")

# User Registration (Sign up) 

def user_sign_up(request):
    if request.method == 'POST':
        user_first_name = request.POST['first name']
        user_last_name = request.POST['last name']
        user_phone_number = request.POST['phone number']
        user_email = request.POST['email']
        username = request.POST['username']
        user_password = request.POST['password']
        try:
            user_obj = User.objects.create(user_name=username, email=user_email)
            user_obj.set_password(user_password)
            user_obj.save()
            user_auth = authenticate(username=username, password=user_password)
            login(request, user_auth)
            return redirect('profile')
        except:
            messages.add_message(request, messages.ERROR, 'Please note that you are unable to register.')
            return render(request,'user_profile/registration.html')
    return render(request,'user_profile/registration.html')

# User Login

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        user_password = request.POST['password']
        try:
            user_obj = authenticate(username=username, password = user_password)
            login (request, user_obj)
            request.session['username'] = username
            return redirect('profile')
        except:
            messages.add_message(request, messages.ERROR, 'Please note that you are unable to login.')
            return render(request,'user_profile/login.html')
    else:
        return render(request,'user_profile/login.html')

# User Logout

def user_logout(request):
    try:
        logout(request)
        messages.add_message(request, messages.INFO, 'You are currently logged out.')
    except:
        messages.add_message(request, messages.ERROR, 'You are unable to logout.')
    return redirect('profile')

# User Profile

@login_required
def user_profile(request,user_id):
    if request.method == 'POST':
        user_obj = User.objects.get(id=user_id)
        user_profile_obj = UserProfile.objects.get(id=user_id)
        user_profile_obj.save()
        user_profile_obj.refresh_from_db()
        return render(request,'user_profile/my_profile.html', {'my_profile': user_profile_obj})
    if (request.user.is_authenticated and request.user.id == user_id):
        user_obj = User.objects.get(id=user_id)
        user_profile = UserProfile.objects.get(id=user_id)
        return render(request, 'user_profile/my_profile.html', {'my_profile': user_profile})
