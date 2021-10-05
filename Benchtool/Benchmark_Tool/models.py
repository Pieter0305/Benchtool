from django.db import models

# Create your models here.
class Userdata(models.Model):
    username = models.CharField(max_length=150)
    device = models.CharField(max_length=150)
    pname = models.CharField(max_length=150)
    cores = models.CharField(max_length=150)
    width = models.CharField(max_length=150)
    arc = models.CharField(max_length=150)
    label = models.TextField(null=True, blank=True)
    float64 = models.TextField(null=True, blank=True)
    int64 = models.TextField(null=True, blank=True)
    int32 = models.TextField(null=True, blank=True)
    int16 = models.TextField(null=True, blank=True)
    

