# Generated by Django 5.0.3 on 2024-04-08 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_pricedetail_company_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricedetail',
            name='company_location',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='pricedetail',
            name='invoice_id',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='pricedetail',
            name='invoice_title',
            field=models.CharField(max_length=255),
        ),
    ]