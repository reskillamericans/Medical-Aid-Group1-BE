from datetime import datetime
from django import forms
from django.forms.widgets import SelectDateWidget, Textarea
from . models import Feedback #, Appointment, Health_Practitioner#, TimeSlots


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = "__all__"
        
    your_name = forms.CharField(max_length=100)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
