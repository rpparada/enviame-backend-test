from django.db import models
from django.db.models.signals import pre_save

from app.utils import unique_slug_generator


# Create your models here.
class Envio(models.Model):

    n_packages = models.IntegerField()
    content_description = models.CharField(max_length=255)
    imported_id = models.CharField(max_length=255)
    order_price = models.IntegerField()
    # order_price = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.CharField(max_length=255)
    volume = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    warehouse_code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    full_address = models.CharField(max_length=255)
    information = models.CharField(max_length=255)
    carrier_code = models.CharField(max_length=255, blank=True, null=True)
    carrier_service = models.CharField(max_length=255, blank=True, null=True)
    tracking_number = models.CharField(max_length=255, blank=True, null=True)

    response = models.TextField(blank=True)

    slug = models.SlugField(blank=True, unique=True)

    fecha_actu = models.DateTimeField(auto_now=True)
    fecha_crea = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return "/enviame/envios/{slug}".format(slug=self.slug)


def envio_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(envio_pre_save_receiver, sender=Envio)
