from django.db import models
from django.contrib.auth.models import User

class Task(models.Model): 
  name = models.CharField(max_length=255)
  done = models.BooleanField(default=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

  def __str__(self):
    return self.name
