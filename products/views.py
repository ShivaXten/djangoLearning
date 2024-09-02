from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def viewAll(request):
    return HttpResponse("This is a demo product to view .")
