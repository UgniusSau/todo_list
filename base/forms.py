from .widgets import  DatePickerInput, TimePickerInput
from django.forms import ModelForm
from .models import Task

class CreateForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'start_date', 'start_date_time', 'end_date','end_date_time', 'complete']

        widgets = {
            'start_date' : DatePickerInput(),
            'start_date_time' : TimePickerInput(),
            'end_date' : DatePickerInput(),
            'end_date_time' : TimePickerInput(),
        }