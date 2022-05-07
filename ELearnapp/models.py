# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Login(models.Model):
    uid = models.CharField(primary_key=True, max_length=15)
    uname = models.CharField(max_length=45)
    toflin = models.DateTimeField()
    toflout = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'login'


class Student(models.Model):
    uid = models.CharField(primary_key=True, max_length=25)
    uname = models.CharField(max_length=45)
    srno = models.IntegerField()
    spno = models.IntegerField()
    sbranch = models.CharField(max_length=45)
    syear = models.CharField(max_length=15)
    spswd = models.CharField(max_length=45)
    sdob = models.DateField()
    snos = models.IntegerField()
    sesubcode = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'student'
        unique_together = (('uid', 'srno'),)


class Vrifylogin(models.Model):
    uid = models.AutoField(primary_key=True)
    upass = models.CharField(max_length=100)
    ukey = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'vrifylogin'


class Work(models.Model):
    workid = models.CharField(primary_key=True, max_length=10)
    dptname = models.CharField(max_length=45)
    subname = models.CharField(max_length=45)
    defwork = models.CharField(max_length=45, blank=True, null=True)
    sdate = models.DateField(blank=True, null=True)
    edate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work'
