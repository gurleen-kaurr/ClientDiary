from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,"index.html")


def clients(request):
     
    if request.method == 'POST':
    # Get form data
    client_name = request.POST.get('client_name')
    client_address = request.POST.get('address')
    client_area = request.POST.get('area')
    client_phno = request.POST.get('phone_number')
    client_service_date = request.POST.get('date')
    client_paymentmode = request.POST.get('payment_mode')

    # Process form data (optional)
    # You can perform validation, save data to a database, etc.

    # Prepare context for displaying form data
    context = {
      'client_name': client_name,
      'client_address': client_address,
      'client_area': client_area,
      'client_phno': client_phno,
      'client_service_date': client_service_date,
      'client_paymentmode': client_paymentmode,
    }

    return render(request, 'clients.html', context)  # Display form data

  else:

    return render(request, 'clients.html', )
