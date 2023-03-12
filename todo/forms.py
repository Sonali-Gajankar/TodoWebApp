from django.forms import ModelForm, widgets
from .models import TodoTasks
import datetime


class TodoTaskForm(ModelForm):
    class Meta:
        model = TodoTasks
        fields = ['title', 'description', 'category', 'date_field', 'starred', 'status']
        widgets = {'date_field': widgets.DateInput(
            attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd', 'class': 'form-control', 'min':datetime.date.today})}
