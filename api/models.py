from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    completed = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.title
