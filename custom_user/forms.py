from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class AdditionForm(UserCreationForm):
    email=forms.EmailField(required=True)
    
    class Meta:
        model=User
        fields=['email', 'password1' ,'password2']
        
'''class CustomLoginForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'autofocus':True}))
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model=CustomUser
        fields=['email', 'password']'''


class CustomLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus': True}))
    password = forms.CharField(widget=forms.PasswordInput)

        