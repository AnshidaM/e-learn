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

class teacher(models.Model):
    tid = models.CharField(max_length = 100)
    tname = models.CharField(max_length=100)
    tpswd = models.CharField(max_length=100)
    tnos =  models.CharField(max_length=100)
    tsubcode =  models.CharField(max_length=100)
    trole =  models.CharField(max_length=100)
    tpno =  models.CharField(max_length=100)
    tdob =  models.CharField(max_length=100)
    tage =  models.CharField(max_length=100)

class student(models.Model):
    sid = models.CharField(max_length = 100)
    sname = models.CharField(max_length=100)
    srno = models.CharField(max_length=100)
    spno =  models.CharField(max_length=100)
    sbranch =  models.CharField(max_length=100)
    syear =  models.CharField(max_length=100)
    spswd =  models.CharField(max_length=100)
    sdob =  models.CharField(max_length=100)
    sage =  models.CharField(max_length=100)
    snos =  models.CharField(max_length=100)
    sesubcode =  models.CharField(max_length=100)
    smark =  models.CharField(max_length=100)  

class subjects(models.Model):
    subcode = models.CharField(max_length=100)
    subname = models.CharField(max_length=100)
    tname =  models.CharField(max_length=100)
    subdrn =  models.CharField(max_length=100)
    submarkd =  models.CharField(max_length=100)
    subnos =  models.CharField(max_length=100)
    subamin =  models.CharField(max_length=100)
    subd =  models.CharField(max_length=100)
    subnom =  models.CharField(max_length=100)
    subnosid =  models.CharField(max_length=100)

class attendance(models.Model):
    sid = models.CharField(max_length = 100)
    subcode = models.CharField(max_length=100)
    tname = models.CharField(max_length=100)
    patdnce =  models.CharField(max_length=100)
    remarks =  models.CharField(max_length=100)

class studymaterials(models.Model):
    subcode = models.CharField(max_length=100)
    mpath = models.CharField(max_length=100)
    mid =  models.CharField(max_length=100)

class tests(models.Model):
     
    sid = models.CharField(max_length=100)
    subcode = models.CharField(max_length=100)
    t1 =  models.CharField(max_length=100)
    t2 =  models.CharField(max_length=100)
    t3 =  models.CharField(max_length=100)
    t1s =  models.CharField(max_length=100)
    t2s =  models.CharField(max_length=100)
    t3s =  models.CharField(max_length=100)
    t1d =  models.CharField(max_length=100)
    t2d =  models.CharField(max_length=100) 
    t3d =  models.CharField(max_length=100)
    sttotal =  models.CharField(max_length=100)
    ttotal =  models.CharField(max_length=100)

class work(models.Model):
     
    sid = models.CharField(max_length=100)
    subcode = models.CharField(max_length=100)
    w1 =  models.CharField(max_length=100)
    w2 =  models.CharField(max_length=100)
    w3 =  models.CharField(max_length=100)
    w1s =  models.CharField(max_length=100)
    w2s =  models.CharField(max_length=100)
    w3s =  models.CharField(max_length=100)
    w1d =  models.CharField(max_length=100)
    w2d =  models.CharField(max_length=100) 
    w3d =  models.CharField(max_length=100)
    swtotal =  models.CharField(max_length=100)
    wtotal =  models.CharField(max_length=100) 

class feedback(models.Model):
    uid = models.CharField(max_length=100)
    fb = models.CharField(max_length=100)
    toffb =  models.CharField(max_length=100)        