from django import forms
from django.contrib.auth import authenticate
from .models import User


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'playername', 'balance')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords don\'t match.')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class DepositForm(forms.Form):
  deposit_amount = forms.FloatField(min_value=1.00, label="Deposit Amount", required=True)

  def clean_deposit_amount(self):
    data = self.cleaned_data['deposit_amount']
    return data
  

class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password, model=User)
            if not user:
                raise forms.ValidationError('Invalid username or password.')
        return cleaned_data
    
class PlayAgainForm(forms.Form):
    user_id = forms.IntegerField(widget=forms.HiddenInput())

  