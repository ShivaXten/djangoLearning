from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
from datetime import datetime
from django.contrib import messages

#this is the navbar section 
def home(request):
        return render (request ,'home.html')

def about(request):
        return render (request ,'about.html')

# def services(request):
#         return render (request ,'services.html')

def frontend(request):
        return render (request ,'services.html')

def backend(request):
        return render (request ,'services.html')

def fullstack(request):
        return render (request ,'services.html')

def contact(request):
        if request.method == "POST":
                name =request.POST.get('name')
                email =request.POST.get('email')
                phone =request.POST.get('phone')
                desc =request.POST.get('desc')
                contact =Contact(name=name, email=email, phone=phone, desc= desc ,date = datetime.today())
                contact.save()
               #this is done to send the messages 
                messages.success(request, "Profile details updated.")
        return render (request ,'contact.html')








