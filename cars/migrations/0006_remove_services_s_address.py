# Generated by Django 4.1.5 on 2023-03-04 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_services_delete_cat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='s_address',
        ),
    ]
