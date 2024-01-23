from django import forms
from .models import *

class Department_form(forms.ModelForm):
    class Meta:
        model = Departments
        fields = '__all__'
    
class Student_form(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'