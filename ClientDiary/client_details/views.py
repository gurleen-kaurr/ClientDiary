from django.shortcuts import render
from django.http import HttpResponse
from .models import * 
from client_details.models import Client

def clients(request):
    return render(request,"clients.html")

def register_client(request):
     
    if request.method == 'POST':

        client_name = request.POST.get('client_name')
        client_address = request.POST.get('client_address')
        client_area = request.POST.get('client_area')
        client_phno = request.POST.get('client_phno')
        client_service_date = request.POST.get('client_service_date')
        client_paymentmode = request.POST.get('client_paymentmode')
        client_staff = request.POST.get('client_staff')

        # Implement form processing logic here (validation, database saving, etc.)
        # ... (e.g., using Django's forms or custom validation)
        # ... (consider saving data to a Django model)

        en =  Client(
            client_name = client_name,
            client_address = client_address,
            client_area = client_area,
            client_phno = client_phno,
            client_service_date = client_service_date,
            client_paymentmode = client_paymentmode,
            client_staff = client_staff
        )
        en.save()

        # Consider rendering a success template or redirecting to a success page
        return render(request, 'client_success.html', context)  # Adjust template name

    else:
        # Handle GET requests (display empty form)
        return render(request, 'clients.html') 
