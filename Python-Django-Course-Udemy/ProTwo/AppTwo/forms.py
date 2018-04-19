from django import forms
from django.core import validators

from . import models

class UserForm(forms.ModelForm):
    botcatcher=forms.CharField(required=False,
                               widget=forms.HiddenInput,
                               validators=[validators.MaxLengthValidator(0)])
    class Meta():
        model=models.User
        fields=['first_name','last_name','email',]
