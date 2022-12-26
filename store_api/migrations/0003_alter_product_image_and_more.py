# Generated by Django 4.1.4 on 2022-12-26 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_api', '0002_product_store'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='store_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
