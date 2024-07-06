from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,"index.html")


def clients(request):
    return render(request, "clients.html")
