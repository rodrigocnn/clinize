from django.db import models


class Agenda(models.Model):

    title = models.CharField(max_length=100, unique=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
