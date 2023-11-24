# Generated by Django 4.1.5 on 2023-02-03 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=122)),
                ('last_name', models.CharField(max_length=122)),
                ('username', models.CharField(max_length=122)),
                ('password', models.CharField(max_length=122)),
                ('address', models.CharField(max_length=122)),
                ('landmark', models.CharField(max_length=122)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('zip', models.IntegerField(max_length=10)),
            ],
        ),
    ]
