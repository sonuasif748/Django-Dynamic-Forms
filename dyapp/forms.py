from django import forms
from django.forms.utils import ErrorList

from dyapp.models import *

class FormResponseform(forms.ModelForm):
    class Meta:
        model = FormResponse
        fields = '__all__'
