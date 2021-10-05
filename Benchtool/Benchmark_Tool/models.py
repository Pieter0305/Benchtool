from django.db import models

# Create your models here.
class Userdata(models.Model):
    username = models.CharField(max_length=150)
    device = models.TextField(null=True, blank=True)
    label = models.TextField(null=True, blank=True)
    float64 = models.TextField(null=True, blank=True)
    int64 = models.TextField(null=True, blank=True)
    int32 = models.TextField(null=True, blank=True)
    int16 = models.TextField(null=True, blank=True)