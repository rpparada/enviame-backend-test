# Generated by Django 2.1.15 on 2021-01-11 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Envio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_packages', models.IntegerField()),
                ('content_description', models.CharField(max_length=255)),
                ('imported_id', models.CharField(max_length=255)),
                ('order_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('weight', models.CharField(max_length=255)),
                ('volume', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('warehouse_code', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=255)),
                ('full_address', models.CharField(max_length=255)),
                ('information', models.CharField(max_length=255)),
                ('carrier_code', models.CharField(max_length=255)),
                ('carrier_service', models.CharField(max_length=255)),
                ('tracking_number', models.CharField(max_length=255)),
            ],
        ),
    ]
