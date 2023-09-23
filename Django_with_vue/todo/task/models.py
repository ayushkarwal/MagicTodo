from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)
    priority = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    completed_on = models.DateTimeField()
