from django.db import models

# Create your models here.

class Entry(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    pub_date = models.DateTimeField()