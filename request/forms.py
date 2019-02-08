from django import forms
from django.forms import ModelForm, FileInput, ClearableFileInput
from bootstrap_datepicker_plus import DatePickerInput
from .models import *


class NewRequestForm(forms.ModelForm):
            
    class Meta:
        model = Request
        fields = ('purpose', 'date_planned', 'amount', 'customer', 'costcenter',)
        widgets = {
            'date_planned': DatePickerInput(
                options={
                    "format": "DD.MM.YYYY",
                    "locale": "ru",
                    "showClose": False,
                    "showClear": False,
                    "showTodayButton": False,
                }),
        }

        

class UploadForm(forms.ModelForm):

    class Meta:
        model = Upload
        fields = ('scan',)
        widgets = {
            'scan' : ClearableFileInput(
                attrs={
                    'multiple': True,
                }),
        }

