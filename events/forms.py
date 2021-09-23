#bu  html faydan turib bazaga malumot qushish uchunn kerak buladi

from django import forms
from django.db import models
from django.forms import ModelForm, fields, widgets
from .models import  Venue, Event

# Venue (joy) form yaratib olish

class VenueForm(ModelForm):
    class Meta: #hardoim
        model = Venue
        fields = '__all__' #barcahsini olib berish uchun xizmat qilai
        
        labels = {
            'name':'Manzil nomi',#bu html kodlar va css kodlarga bog'lash uchun
            'address':'Manzil qacherda?',
            'phone':'Telefon raqami',
            'email_address':'Email manzilli',            
        }

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),#bu html kodlar va css kodlarga bog'lash uchun
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'email_address':forms.EmailInput(attrs={'class':'form-control'}),
        }


class EventForm(ModelForm):
    class Meta: #hardoim
        model = Event
        fields = '__all__' #barcahsini olib berish uchun xizmat qilai
        
        labels = {
            'name':'Hodisa nomi?',#bu html kodlar va css kodlarga bog'lash uchun
            'event_date':'Qachon? YYYY-MM-DD',
            'venue':'Qayerda?',
            'description':'Batafsil malumot!', 
            'manager':'Tashkilotchilar',  
            'attendees':'Qatnashuvchilar'     
        }

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),#bu html kodlar va css kodlarga bog'lash uchun
            'event_date':forms.TextInput(attrs={'class':'form-control'}),
            'venue':forms.Select(attrs={'class':'form-select'}),
            'manager':forms.Select(attrs={'class':'form-select'}),
            'attendees':forms.SelectMultiple(attrs={'class':'form-select'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
        }
