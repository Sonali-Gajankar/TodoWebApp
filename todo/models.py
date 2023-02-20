import datetime

from django.db import models
from django.urls import reverse
from users.models import CustomUser


# Create your models here.
class TodoTasks(models.Model):
    CATEGORY_CHOICES = [
        ('Personal', 'Personal'), ('Work', 'Work'), ('Study', 'Study'), ('Misc', 'Miscellaneous')
    ]
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, blank=False, default=CATEGORY_CHOICES[0])
    starred = models.BooleanField(default=False)
    date_field = models.DateField(default=datetime.date.today)
    status = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('task-list')
