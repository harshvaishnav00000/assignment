from django.db import models

class Client(models.Model):
    email = models.CharField(max_length=70)
    password = models.CharField(max_length=70)

class User(models.Model):
    emailaddress = models.CharField(max_length=70, null=True, blank=True)
    startdate = models.CharField(max_length=70, null=True, blank=True)
    dates = models.CharField(max_length=70, default="none", null=True, blank=True)
    shift = models.CharField(max_length=70, default="none", null=True, blank=True)
    starttime = models.CharField(max_length=70, null=True, blank=True)
    endtime = models.CharField(max_length=70,null=True, blank=True)
    days = models.CharField(max_length=70, default="none", null=True, blank=True)
