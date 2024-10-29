from django import forms
from .models import User

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=255)