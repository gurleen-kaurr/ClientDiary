from django.urls import path
from django.shortcuts import render, redirect
from ClientDiary.settings import mongo_db  # Import mongo_db directly

def list_clients(request):
    clients = mongo_db.clients.find()
    return render(request, 'admin/list_clients.html', {'clients': clients})

def delete_client(request, client_id):
    mongo_db.clients.delete_one({'_id': client_id})
    return redirect('admin_list_clients')

urlpatterns = [
    path('admin/clients/', list_clients, name='admin_list_clients'),
    path('admin/clients/delete/<client_id>/', delete_client, name='admin_delete_client'),
]