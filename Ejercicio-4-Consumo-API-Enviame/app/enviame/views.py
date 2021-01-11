from enviame import services

from django.views.generic import CreateView, DetailView, ListView
from django.shortcuts import render
from django.http import Http404

from enviame.models import Envio
from enviame.forms import CreateEnvioForm


# Create your views here.
class CreateEnvioView(CreateView):

    form_class = CreateEnvioForm
    template_name = 'enviame/creaenvio.html'


class EnvioDetailView(DetailView):

    template_name = 'enviame/envio.html'

    def get_object(self, queryset=None):

        slug = self.kwargs.get('slug')

        try:
            envio = Envio.objects.get(slug=slug)
        except Envio.DoesNotExist:
            raise Http404('Envio No encontrado')
        except Envio.MultipleObjectsReturned:
            envios = Envio.objects.filter(slug=slug)
            envio = envios.first()
        except Exception:
            raise Http404('Error Desconocido')

        return envio


class EnvioListView(ListView):

    queryset = Envio.objects.all()
    template_name = 'enviame/envios.html'
    ordering = ['n_packages']


def home(request):

    params = {
        'n_packages': 1,
        'content_description': 'ORDEN 255826267',
        'imported_id': '255826267',
        'order_price': 24509.0,
        'weight': '0.98',
        'volume': '1.0',
        'type': 'delivery',
        'warehouse_code': '401',
        'name': 'Bernardita Tapia Riquelme,',
        'email': 'b.tapia@outlook.com',
        'phone': '977623070',
        'place': 'Puente Alto',
        'full_address': 'SAN HUGO 01324, Puente Alto, Puente Alto',
        'information': '',
        'carrier_code': 'SKN',
        'carrier_service': '',
        'tracking_number': ''
    }

    envio = services.crear_envio_como_seller(params=params)
    print(envio)
    context = {
    }
    return render(request, "enviame/creaenvio.html", context)
