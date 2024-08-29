from django.urls import path
from .import views

urlpatterns=[
    path('',views.homeTemp, name="homeTemp"),
    path('room/',views.room, name="room"),
    path('RoomTemp/',views.roomTemp, name="roomTemp"),
 
 
    
    
]
