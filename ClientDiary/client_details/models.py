from django.db import models

class Client(models.Model):
    client_name = models.CharField(max_length=150)
    client_address = models.TextField()
    client_area = models.CharField(max_length=100)
    client_phno = models.IntegerField(max_length=10)
    client_service_date = models.DateField()
    client_paymentmode = models.BooleanField(default=False)