import requests


def crear_envio_como_seller(params):
    ''' Crea envio como seller Enviame API '''

    url = 'https://stage.api.enviame.io/api/s2/v2/companies/401/deliveries'

    headers = {
        'Accept': 'application/json',
        'api-key': 'ea670047974b650bbcba5dd759baf1ed',
        'Content-Type': 'application/json'
    }

    payload = {
        "shipping_order": {
            "n_packages": params['n_packages'],
            "content_description": params['content_description'],
            "imported_id": params['imported_id'],
            "order_price": params['order_price'],
            "weight": params['weight'],
            "volume": params['volume'],
            "type": params['type']
        },
        "shipping_origin": {
            "warehouse_code": params['warehouse_code']
        },
        "shipping_destination": {
            "customer": {
                "name": params['name'],
                "email": params['email'],
                "phone": params['phone']
            },
            "delivery_address": {
                "home_address": {
                    "place": params['place'],
                    "full_address": params['full_address'],
                    "information": params['information']
                }
            }
        },
        "carrier": {
            "carrier_code": params['carrier_code'],
            "carrier_service": params['carrier_service'],
            "tracking_number": params['tracking_number']
        }
    }

    response = requests.request("POST", url, headers=headers, json=payload)
    envio = response.json()

    return envio
