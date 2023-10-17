from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    ism = models.CharField(max_length=150)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tel_raqam = models.CharField(max_length=15, blank=True)
    jins = models.CharField(max_length=6)
    shahar = models.CharField(max_length=150)
    davlat = models.CharField(max_length=150)
    sms_kod = models.CharField(max_length=150)
    tasdiqlangan = models.BooleanField(default=False)

    def __str__(self):
        return self.ism