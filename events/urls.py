from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name = "home" ),
    path('<int:year>/<str:month>/', views.home, name = "home" ),
    path('events/',views.all_events, name='list-events'),
    path('add_venue/', views.add_venue,name='add-venue'),
    path('list_venue/', views.list_venue,name='list-venue'),
    #< parametr olamiz >
    path('show_venue/<venue_id>', views.show_venue,name='show-venue'),  #name bu yerda htmldagi  href="{% url 'add_venue' %} linki uchun kerak
    path('search_venue/',views.search_venue,name='Search'),
    path('update/<venue_id>', views.update_venue,name='update-venue'),
    path('add_event/', views.add_event,name='add-event'),
    path('update_event/<event_id>', views.update_event,name='update-event'),
    path('delete_event/<event_id>',views.delete_event, name='delete-event'),
    path('delete_venue/<venue_id>',views.delete_venue, name='delete-venue'),
    path('venue_text',views.venue_text,name='venue-text'),
    path('venue_cvs',views.venue_cvs,name='venue-cvs'),
    path('venue_pdf',views.venue_pdf,name='venue-pdf')
]