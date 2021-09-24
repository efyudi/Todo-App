from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.conf import settings


class TodoModel(models.Model):
    name = models.CharField(max_length=200)
    option = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, db_column='user')

    # Either provide success_url in View, or set override the below method
    def get_absolute_url(self):
        return reverse('todo_home')
    
    def __str__(self):
        return self.name
