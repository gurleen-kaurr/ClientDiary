from django.shortcuts import render
from django.http import HttpResponse
from .models import * 
from client_details.models import Client


def home(request):
    return render(request,"index.html")

def clients(request):
    return render(request=clients.html)




