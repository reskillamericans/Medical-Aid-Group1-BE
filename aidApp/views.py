from django.shortcuts import render
from .forms import FeedbackForm #,DocProfileForm, AppointmentForm
from django.http import HttpResponse, HttpResponseRedirect
#from . models import Health_Practitioner


def index(request):
    return HttpResponse("<h1>Medical Aid app Homepage</h1>")


def Feedback(request):
    context = {}
    submitted = False
    
    if request.method == 'POST':
         form = FeedbackForm(request.POST)
         if form.is_valid():
            form.save()
            
            return HttpResponseRedirect('feedback?submitted=True')

         else:
            return render(request,'feedback.html',{'form': form})
 
    context = {'form': FeedbackForm(),
               'submitted': submitted
              }
    return render(request, 'feedback.html', context) 

