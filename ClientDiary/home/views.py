from django.shortcuts import render
from django.http import HttpResponse
from home.models import * 
from client_details.models import Client


def home(request):
    return render(request,"index.html")

def search_feature(request):
    # Check if the request is a post request.
    if request.method == 'POST':
        # Retrieve the search query entered by the user
        search = request.POST['search']
        # Filter your model by the search query
        posts = Model.objects.filter(fieldName__contains=search)
        return render(request, 'searched_details.html', {'query':search, 'posts':posts})
    else:
        return render(request, 'searched_details.html',{})
