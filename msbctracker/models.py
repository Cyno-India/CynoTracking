from email.policy import default
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Tracker(models.Model):
    status = models.CharField(default="", max_length=20)
    api_call_time = models.CharField(default="",max_length=10)
    tracking_number = models.CharField(default="", max_length=20, unique=True)
    updated_time = models.CharField(default="",max_length=10)
    booked = models.CharField(default="", max_length=20)
    arrival = models.CharField(default="", max_length=20)
    delivered = models.CharField(default="", max_length=20)
    outbound = models.CharField(default="", max_length=20)
    tracking_info = models.JSONField(default="")
    msbc_patch_api_call_time=models.CharField(default="",max_length=10)
    numeric_status = models.IntegerField(default="", max_length=20)


class Logs(models.Model):
    tracking_logs = models.JSONField(default="")
    api_call_time = models.CharField(default="",max_length=10)


