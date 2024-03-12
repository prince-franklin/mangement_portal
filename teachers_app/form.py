from django import forms
from . models import student_profile, courses_detail,department_mod

class studentForm(forms.ModelForm):
    class Meta:
        model= student_profile
        fields=['name','email', 'courses', 'phone']
        
class courseForm(forms.ModelForm):
    class Meta:
        model=courses_detail
        fields=['title', 'code','description','department','teacher']
        
        
class departmentForm(forms.ModelForm):
    class Meta:
        model=department_mod
        fields=['department']