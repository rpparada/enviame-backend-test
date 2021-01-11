from django import forms

from enviame.models import Envio

from enviame import services


class CreateEnvioForm(forms.ModelForm):

    n_packages = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
    }), label='Numero Paquete')
    content_description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }), label='Descripcion')
    imported_id = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }), label='ID')
    order_price = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
    }), label='Precio Orden')
    # order_price = forms.DecimalField(widget=forms.NumberInput(attrs={
    #     'class': 'form-control',
    # }), label='Precio Orden')
    weight = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }), label='Peso')
    volume = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }), label='Volumen')
    type = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }), label='Tipo')
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }), label='Nombre')
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }), label='Telefono')
    place = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }), label='Comuna')
    full_address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }), label='Direccion')
    information = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }), label='Informacion')

    class Meta:
        model = Envio
        exclude = (
            'slug',
            'response',
            'carrier_code',
            'carrier_service',
            'tracking_number',
            'warehouse_code'
        )

    def save(self, commit=True):
        envio = super(CreateEnvioForm, self).save(commit=False)

        params = {
            'n_packages': envio.n_packages,
            'content_description': envio.content_description,
            'imported_id': envio.imported_id,
            'order_price': envio.order_price,
            'weight': envio.weight,
            'volume': envio.volume,
            'type': envio.type,
            'warehouse_code': '401',
            'name': envio.name,
            'email': envio.email,
            'phone': envio.phone,
            'place': envio.place,
            'full_address': envio.full_address,
            'information': envio.information,
            'carrier_code': 'SKN',
            'carrier_service': '',
            'tracking_number': ''
        }

        envio_api = services.crear_envio_como_seller(params=params)

        envio.response = envio_api

        if commit:
            envio.save()

        return envio
