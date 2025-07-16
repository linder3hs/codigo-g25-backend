import mercadopago
from django.conf import settings

class MercadoPagoService:
    """
    Servicio para implementar pasarelas de pago en mi appliación
    """

    def __init__(self):
        self.sdk = mercadopago.SDK(settings.MERCADOPAGO_ACCESS_TOKEN)


    def create_preference(self, items, order_data):
        """
        Preferencia de mercadopago
        """
        try:
            preference_data = {
                "items": items,
                "back_urls": {
                    "success": f"{settings.BASE_URL}/api/payments/success/",
                    "failure": f"{settings.BASE_URL}/api/payments/failure/",
                    "pending": f"{settings.BASE_URL}/api/payments/pending/"
                },
                "auto_return": "approved",
                "external_reference": str(order_data.get('order_id')),
                "payer": {
                    "name": order_data.get('customer_name', ''),
                    "email": order_data.get('customer_email', ''),
                    "phone": {
                        "area_code": "51",
                        "number": order_data.get('customer_phone', '')
                    }
                },
                "notifiaction_url": f"{settings.BASE_URL}/api/payments/webhook",
                "payment_methods": {
                    "excluded_payment_methods": [],
                    "excluded_payment_types": [],
                    "installments": 12
                }
            }
        except Exception as e:
            print(f"Error: {e}")
