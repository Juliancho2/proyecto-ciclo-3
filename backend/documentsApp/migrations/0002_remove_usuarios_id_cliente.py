# Generated by Django 4.1.2 on 2022-10-11 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documentsApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='id_cliente',
        ),
    ]
