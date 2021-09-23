from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
# Create your models here.

class Venue(models.Model):
    name = models.CharField('Venue name',max_length=120,blank=True)
    address = models.CharField(max_length=300,blank=True)
    phone = models.CharField('Contact number:', max_length=25,blank=True)
    email_address = models.EmailField('Email address',blank=True)

    def __str__(self):
        return self.name

class MyClubUser(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email_address = models.EmailField('Email address')

    def __str__(self):
        return self.fname+' '+self.lname


class Event(models.Model):
    name = models.CharField('Event name:', max_length=120)
    event_date = models.DateTimeField('Event Date')

    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    #venue = models.CharField(max_length=120)

    #ForeignKey
    manager = models.ForeignKey(User,blank=True,null=True,on_delete=models.SET_NULL )

    attendees = models.ManyToManyField(MyClubUser, blank=True)
    
    description = models.TextField(blank=True)    
    def __str__(self):
        return self.name