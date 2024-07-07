from django.contrib import admin
from client_details.models import Client

class ClientAdmin(admin.ModelAdmin):
     list_display=('client_address', 
                   'client_area' ,  
                   'client_phno', 
                   'client_service_date',
                   'client_paymentmode')
admin.site.register(Client,ClientAdmin)
