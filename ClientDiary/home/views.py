from django.shortcuts import render
from django.http import HttpResponse
from home.models import * 



def home(request):
    return render(request,"index.html")




