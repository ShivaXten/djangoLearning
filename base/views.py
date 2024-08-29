from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

# Create your views here.

def room(request):
        return HttpResponse('Room')



#this is the navbar section 
def home(request):
        return render (request ,'home.html')

def about(request):
        return render (request ,'about.html')

def contact(request):
        return render (request ,'contact.html')

# def services(request):
#         return render (request ,'services.html')

def frontend(request):
        return render (request ,'services.html')

def backend(request):
        return render (request ,'services.html')

def fullstack(request):
        return render (request ,'services.html')








