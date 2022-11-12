from django import forms
from django.forms import TimeInput

widget = TimeInput(format='%H:%M', attrs={'type': 'time'})
class DatePickerInput(forms.DateInput):
        input_type = 'date'

class TimePickerInput(forms.TimeInput):
        input_type = 'time'
        
        