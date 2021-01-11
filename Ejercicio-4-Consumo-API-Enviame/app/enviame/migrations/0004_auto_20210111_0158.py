# Generated by Django 2.1.15 on 2021-01-11 01:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('enviame', '0003_envio_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='envio',
            name='fecha_actu',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='envio',
            name='fecha_crea',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]