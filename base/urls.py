from django.urls import path
from .import views

urlpatterns=[
    path('',views.home, name="home"),
    path('room/',views.room, name="room"),
    path('homeTemp/',views.homeTemp, name="homeTemp"),
    path('RoomTemp/',views.roomTemp, name="roomTemp"),
 
 
    
    
]
