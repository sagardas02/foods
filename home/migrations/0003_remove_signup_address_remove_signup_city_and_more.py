# Generated by Django 4.1.5 on 2023-02-03 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_signup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='address',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='city',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='landmark',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='password',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='state',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='username',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='zip',
        ),
    ]
