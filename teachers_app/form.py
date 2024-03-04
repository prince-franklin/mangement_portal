from django import forms
from . models import student_profile, courses_detail

class studentForm(forms.ModelForm):
    class Meta:
        model= student_profile
        fields=['name','email', 'courses', 'phone']
        
class courseForm(forms.ModelForm):
    class Meta:
        model=courses_detail
        fields=['title', 'code','description','department','teacher']