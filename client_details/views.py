from django.shortcuts import render
from django.http import HttpResponse
from .models import Client
from ClientDiary.settings import mongo_db  # Import mongo_db directly

def clients(request):
    return render(request, "clients.html")

def register_Client(request):
    if request.method == 'POST':
        client_name = request.POST.get('client_name')
        client_address = request.POST.get('client_address')
        client_area = request.POST.get('client_area')
        client_phno = request.POST.get('client_phno')
        client_service_date = request.POST.get('client_service_date')
        client_paymentmode = request.POST.get('client_paymentmode')
        client_staff = request.POST.get('client_staff')

        en = Client(
            client_name=client_name,
            client_address=client_address,
            client_area=client_area,
            client_phno=client_phno,
            client_service_date=client_service_date,
            client_paymentmode=client_paymentmode,
            client_staff=client_staff
        )
        en.save()

        context = {'message': 'Client registration successful!'}
        return render(request, 'success.html', context)  # Adjust template name

    else:
        # Handle GET requests (display empty form)
        return render(request, 'clients.html')

def search(request):
    if 'query' in request.GET:
        query = request.GET['query']
        client = mongo_db.clients.find({
            "client_name": query
        })
    else:
        client = mongo_db.clients.find()

    context = {'client': list(client)}
    return render(request, 'searched_detail.html', context)