from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=50)
    state = models.IntegerField()
    dead_line = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
