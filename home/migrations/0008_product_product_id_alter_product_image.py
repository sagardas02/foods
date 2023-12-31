# Generated by Django 4.1.5 on 2023-02-04 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_id',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='static/images'),
        ),
    ]
