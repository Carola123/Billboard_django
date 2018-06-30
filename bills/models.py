from django.db import models

class Bill(models.Model):
    date = models.DateTimeField('date published')
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=600)
    author = models.CharField(max_length=30)
