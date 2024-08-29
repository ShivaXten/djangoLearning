from django.urls import path
from .import views

urlpatterns=[
    path('room/',views.room, name="room"),

    #this is the navbar section 
    path('',views.home, name="home"),
    path('about/',views.about, name="about"),
    path('contact/',views.contact, name="contact"),
    #path('services/',views.services, name="services"),
     path('frontend/',views.frontend, name="frontend"),
    path('backend/',views.backend, name="backend"),
    path('fullstack/',views.fullstack, name="fullstack"),
  

 
 
    
    
]
