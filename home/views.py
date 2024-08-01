from django.shortcuts import render
from django.http import HttpResponse
from home.models import * 
from client_details.models import Client


def home(request):
    return render(request,"index.html")


