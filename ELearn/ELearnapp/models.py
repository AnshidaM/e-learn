from django.db import models
class verifylogin(models.Model):
    uname = models.CharField(max_length = 100)
    epass = models.CharField(max_length=100)
    ukey = models.CharField(max_length=1)
