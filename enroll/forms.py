from django import forms
# from django.core import validators 
from enroll.models import user

class Student(forms.ModelForm):
    class Meta:
        model=user
        fields=['name','email','password']
        # widgets={
        #     'name':forms.TextInput(attrs={'class':'form-control'}),
        #     'email':forms.EmailField(attrs={'class':'form-control'}),
        #     'password':forms.PasswordInput(attrs={'class':'form-control'}),
        # }