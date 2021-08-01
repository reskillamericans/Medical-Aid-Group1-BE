from django import forms
from django.db.models import fields
from django.forms import widgets
from django.forms import ModelForm, TextInput, EmailInput
from django.forms.widgets import Select, Textarea
from . models import Contact


class CreateContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {'fname': TextInput(attrs={'class': "input-container", 'style': "margin-right: 100px"}),
                   'lname': TextInput(attrs={'class': "input-container"}),
                   'email': EmailInput(attrs={'class': "input-container", 'style': "margin-right: 100px"}),
                   'inquiry': Select(attrs={'class':"dropdown", 'style': "margin-right: 56px", 'width': '100%', 'text-align': 'center'}),
                   'subject': TextInput(attrs={'class': "input-container"}),
                   'comment': Textarea(attrs={'height': '215px', 'width': '390px'})        
        }

    