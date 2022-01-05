from django.db import models


class Task(models.Model):
    task = models.CharField(null=False, blank=False, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    checked = models.BooleanField(default=False)


class Todo(models.Model):
    task = models.ManyToManyField(Task)
