from django.db import models

# Create your models here.
class Task(models.Model):
    taskTitle = models.CharField(max_length=200)
    taskContent = models.TextField()
    taskComplete = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str.text