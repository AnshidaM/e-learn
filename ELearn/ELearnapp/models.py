from django.db import models
class verifylogin(models.Model):
    uname = models.CharField(max_length = 100)
    epass = models.CharField(max_length=100)
    ukey = models.CharField(max_length=1)
    
class login(models.Model):
    uid = models.CharField(max_length = 100)
    toflin = models.CharField(max_length=50)
    toflout = models.CharField(max_length=50)
    
class admin(models.Model):
    adid = models.CharField(max_length = 100)
    adname = models.CharField(max_length=100)
    adpswd = models.CharField(max_length=100)
    adpno =  models.CharField(max_length=100)
    