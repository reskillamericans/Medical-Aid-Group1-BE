from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['full_name', 'email', 'password1', 'password2']

    full_name = forms.Field(widget=forms.TextInput(attrs={
        'class': 'form info', 'placeholder': 'Full Name'
    }))
    email = forms.Field(widget=forms.EmailInput(attrs={
        'class': 'form info', 'placeholder': 'Email Address'
    }))
    password1 = forms.Field(widget=forms.PasswordInput(attrs={
        'class': 'form info', 'placeholder': 'Password'
    }),label = 'Password')
    password2 = forms.Field(widget=forms.PasswordInput(attrs={
        'class': 'form info', 'placeholder': 'Password'
    }),label = 'Confirm Password')
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.username = instance.email
        if commit:
            instance.save()
        return instance