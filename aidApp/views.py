from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

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
    return render(request, 'aidApp/doctor/doctor-search.html')

def doctor_appointment_view(request):
    return render(request, 'aidApp/doctor/doctor-appointment.html')

def patient_support_view(request):
    if request.method == "POST":
        if request.POST.get('fullname') and request.POST.get('message'):
            support = Feedback()
            support.fullname = request.POST.get('fullname')
            support.email = request.POST.get('email')
            support.complaint = request.POST.get('complaint')
            support.message = request.POST.get('message')
            support.save()
            return render(request, 'aidApp/patient/patient-support.html')            
    else:
        return render(request, 'aidApp/patient/patient-support.html')