from django import forms
from django.forms import ModelForm
from bootstrap_datepicker_plus import DatePickerInput
from .models import *

class RequestForm(forms.ModelForm):

    class Meta:
        model = Request
        exclude = ['author']
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


