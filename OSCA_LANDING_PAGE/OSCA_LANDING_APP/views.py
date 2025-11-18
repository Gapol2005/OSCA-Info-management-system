from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    from django.http import HttpResponse
    return HttpResponse("Welcome to the OSCA Landing Page")