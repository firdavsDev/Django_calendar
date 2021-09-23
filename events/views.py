import calendar
from django.shortcuts import render,redirect

# Create your views here.
from datetime import datetime
from calendar import HTMLCalendar

from reportlab.lib import pagesizes
from .forms import VenueForm, EventForm

#model faylani import qilamiz....
from .models import Event, Venue
from django.http import HttpResponseRedirect, response

#TXT fayl uchun
from django.http import HttpResponse, FileResponse

#PIP INSTALL reportlab
#PDF FAYLDA MALUMOTNI OLISH UCHUN
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter



#Excel faylar uchun
import csv

#teks faylar bn ishlash uchun kerak buladi
def venue_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename = venue.txt'

    venues = Venue.objects.all()

    lines = [f'{venue.name}\n{venue.address}\n{venue.phone}\n{venue.email_address}\n\n\n' for venue in venues]
    #Text faylga yozish
    response.writelines(lines)
    return response


#Exelda kursatish malumotarni
def venue_cvs(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename = venue.csv'

    #csv faylga yozish
    writer = csv.writer(response)

    #saytdagi malumotlarimiz
    venues = Venue.objects.all()

    #csv faylga ustun qushish
    writer.writerow(["Manzil nomi", 'Manzil','Telefon','Email'])

    
    for venue in venues:
        writer.writerow([venue.name, venue.address, venue.phone, venue.email_address])

    return response

#PDF faylga yozish malumotlarni
#PIP INSTALL reportlab

def venue_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)

    #TExt object yaratish
    textob = c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont('Helvetica',14)



    venues = Venue.objects.all()

    lines = []

    for venue in venues:
        lines.append(' ')
        lines.append(venue.name)
        lines.append(venue.address)
        lines.append(venue.phone)
        lines.append(venue.email_address)
        lines.append('=========================================')

    #Looop
    for line in lines:
        textob.textLine(line)

    #tugatish
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    #retuen

    return FileResponse(buf,as_attachment=True,filename='venue.pdf')



#barcha eventlar uchun
def all_events(request):
    event_list = Event.objects.all().order_by('name') #tartiblash uchun kerak
    return render(request,'events/event.html',{'event_list':event_list})

#manzilarni kursatiw uchun
def show_venue(request,venue_id):
    venue = Venue.objects.get(pk=venue_id)
    return render(request,'events/show_venue.html',{'venue':venue})

# barcha venues(joylar)
def list_venue(request):
    venue_list = Venue.objects.all().order_by('name') # ? agar suroq belgisi bulsa random bulib qoladi
    return render(request,'events/joy.html',{'venue_list':venue_list})


#home uchun
def home(request, year=datetime.now().year,month=datetime.now().strftime('%B')):

    #oyni raqamga olyamiz
    month = month.capitalize()
    month_num = list(calendar.month_name).index(month)
    month_num = int(month_num)

    #calendar yasaymiz
    cal = HTMLCalendar().formatmonth(year,month_num)

    #hozirgi vaqt
    now = datetime.now()
    current_day = now.date()
    #current_time = now.strftime("%H:%M")

    context = {
        'calendar':cal,
        'month':month,
        'year': year,
        'now':current_day
    }

    return render(request, 'events/home.html',context)



#manzil qushadi
def add_venue(request):
    submitted = False
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True
    context = {
    'form':form,
    'submitted':submitted
    }
    return render(request,'events/ad_joy.html',context)

#hodisalar qushish uchun
def add_event(request):
    submitted = False
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True
    context = {
    'form':form,
    'submitted':submitted
    }
    return render(request,'events/add_event.html',context)


#qidiruv
def search_venue(request):  # sourcery skip
    if request.method == 'POST':
        searched = request.POST['searched'] #.capitalize() #html kod ichidagi inputga name='searched' briladigani
        venue = Venue.objects.filter(name = searched)
        return render(request, 'events/search.html',{'searched':searched,'venue':venue})
    else:
        return render(request, 'events/search.html',{})

#Yangilash mazilarni
def update_venue(request,venue_id):
    venue = Venue.objects.get(pk=venue_id) #bazadan izlash
    form = VenueForm(request.POST or None, instance=venue)#instance eski bazadagi holatidagi kabi keltib beradi
    if form.is_valid():
        form.save()
        return redirect('list-venue') #urls dagi path ni name= yoziladi redirect ichida
    return render(request,'events/update_venue.html',{'venue':venue,'form':form})

#hodisalarni yangilash uchun kerak buladdidgan
def update_event(request,event_id):
    event = Event.objects.get(pk=event_id) #bazadan izlash
    form = EventForm(request.POST or None, instance=event)#instance eski bazadagi holatidagi kabi keltib beradi
    if form.is_valid():
        form.save()
        return redirect('list-events') #urls dagi path ni name= yoziladi redirect ichida
    return render(request,'events/update_event.html',{'event':event,'form':form})

#uchirish uchun krak buladi
def delete_event(request,event_id):
    deletevent = Event.objects.get(pk=event_id)
    deletevent.delete() #uchirish uchun
    return redirect('list-events')

#For delete itms
def delete_venue(request,venue_id):
    deletevenue = Venue.objects.get(pk=venue_id)
    deletevenue.delete() #uchirish uchun
    return redirect('list-venue')