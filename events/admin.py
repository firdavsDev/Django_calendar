from django.contrib import admin
from django.db import models

from .models import Venue, MyClubUser, Event


# Register your models here.

#admin.site.register(Venue)
#admin.site.register(Event)
admin.site.register(MyClubUser)


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name','address','phone')
    #tartiblash uchun ('-name') z-a
    ordering = ('name',) 
    search_fields = ('name', 'address') #izlash


@admin.register(Event)
class EventAdminn(admin.ModelAdmin):
    fields = (('name','venue'),'event_date','description','manager')
    list_display = ('name','event_date','venue')
    list_filter = ('event_date','venue')
    ordering = ('-event_date',)