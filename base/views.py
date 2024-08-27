from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
        return HttpResponse('Home Page')

def room(request):
        return HttpResponse('Room')

def homeTemp(request):
        return render (request ,'homeTemp.html')

def roomTemp(request):
        return render (request,'RoomTemp.html')



