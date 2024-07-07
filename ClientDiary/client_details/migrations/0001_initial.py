# Generated by Django 2.2.28 on 2024-07-07 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=150)),
                ('client_address', models.TextField()),
                ('client_area', models.CharField(max_length=100)),
                ('client_phno', models.IntegerField(max_length=10)),
                ('client_service_date', models.DateField()),
                ('client_paymentmode', models.BooleanField(default=False)),
            ],
        ),
    ]
