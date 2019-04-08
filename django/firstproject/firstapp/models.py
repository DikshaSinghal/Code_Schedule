from django.db import models
from django.conf import settings

class Contests(models.Model):
    Website = models.CharField(max_length=200,default='DEFAULT VALUE')
    contestname = models.CharField(max_length=200,default='DEFAULT VALUE')
    date = models.CharField(max_length=200,default='DEFAULT VALUE')
    time = models.CharField(max_length=200,default='DEFAULT VALUE')
    link = models.CharField(max_length=200,default='DEFAULT VALUE')

    def __str__(self):
        return self.contestname
