# Generated by Django 5.0.1 on 2024-02-13 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_pricedetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricedetail',
            name='company_name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='pricedetail',
            name='invoice_id',
            field=models.CharField(default=500, max_length=50),
        ),
    ]
