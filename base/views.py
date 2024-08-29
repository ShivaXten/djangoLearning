from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

# Create your views here.

def room(request):
        return HttpResponse('Room')

def homeTemp(request):
        return render (request ,'homeTemp.html')

def roomTemp(request):
        return render (request,'RoomTemp.html')





