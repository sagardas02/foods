# Generated by Django 4.1.5 on 2023-02-04 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_orders_delete_signup'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.CharField(default='', max_length=20),
        ),
    ]