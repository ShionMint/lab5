from django.db import models
import datetime

# Create your models here.

class Owner(models.Model):
    type_owner = models.CharField(max_length=120)
    name_owner = models.CharField(max_length=120)
    full_name = models.CharField(max_length=120)
    contact_number = models.CharField(max_length=120)
    opening_date = models.DateField(default=datetime.date.today)
    objects = models.Manager()

class Object(models.Model):
    owner_id = models.ForeignKey('Owner', on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    type = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    number_of_seats = models.IntegerField()
    objects = models.Manager()

class Event(models.Model):
    object_id = models.ForeignKey('Object', on_delete=models.CASCADE)
    date_of_event = models.DateField(default=datetime.date.today)
    type_of_event = models.CharField(max_length=120)
    objects = models.Manager()

class Popularity(models.Model):
    object_id = models.ForeignKey('Object', on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    number_of_visitors = models.IntegerField()
    objects = models.Manager()

class Users(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=120)
    position = models.CharField(max_length=120)
    login = models.CharField(max_length=120)
    password = models.IntegerField()
    objects = models.Manager()

class Backup_copy(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=120)

