from django.forms import ModelForm, SelectDateWidget
from .models import TodoTasks


class TodoTaskForm(ModelForm):
    class Meta:
        model = TodoTasks
        fields = ['title', 'description', 'category', 'date_field', 'starred', 'status']
        widgets = {'date_field': SelectDateWidget()}
