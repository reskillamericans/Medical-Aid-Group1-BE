from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Landing page 
def index(request):
    return render(request, 'index.html')

# About Us page 
def about_us(request):
    return render(request, 'about-us.html')

# ADMIN VIEWS
def admin_views(request):
    return render(request, 'Admin/admin-dash.html')
