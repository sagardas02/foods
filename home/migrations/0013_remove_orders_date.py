# Generated by Django 4.1.5 on 2023-02-10 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_orders_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='date',
        ),
    ]
