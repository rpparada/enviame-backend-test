# Generated by Django 2.1.15 on 2021-01-11 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enviame', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='envio',
            name='response',
            field=models.TextField(blank=True),
        ),
    ]
