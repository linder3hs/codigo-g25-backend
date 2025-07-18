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
                # "back_urls": {
                #     "success": f"{settings.BASE_URL}/api/payments/success/",
                #     "failure": f"{settings.BASE_URL}/api/payments/failure/",
                #     "pending": f"{settings.BASE_URL}/api/payments/pending/"
                # },
                # "auto_return": "approved",
                "external_reference": str(order_data.get('order_id')),
                "payer": {
                    "name": order_data.get('customer_name', ''),
                    "email": order_data.get('customer_email', ''),
                    "phone": {
                        "area_code": "51",
                        "number": order_data.get('customer_phone', '')
                    }
                },
                "notification_url": f"{settings.BASE_URL}/api/payments/webhook/",
                "payment_methods": {
                    "excluded_payment_methods": [],
                    "excluded_payment_types": [],
                    "installments": 12
                }
            }

            response = self.sdk.preference().create(preference_data)

            # status === 201 (created)
            if response["status"] == 201:
                preference = response["response"]

                return {
                    "success": True,
                    "preference_id": preference["id"],
                    "init_point": preference["init_point"],
                    "sandbox_init_point": preference["sandbox_init_point"]
                }

            return {
                "success": False,
                "error": "Error al crear la preferencia en Mercado Pago",
                "detail": response
            }
        except Exception as e:
            print(f"Error: {e}")
            return {
                "success": False,
                "error": f"Error {e}",
            }

    def get_payment_info(self, payment_id):
        """
        Obtener el detalle de un pago
        """
        try:
            response = self.sdk.payment().get(payment_id)
            # 200 (ok)
            if response["status"] == 200:
                payment = response["payment"]
                return {
                    "success": True,
                    "payment": {
                        "id": payment["id"],
                        "status": payment["status"],
                        "status_detail": payment["status_detail"],
                        "external_reference": payment["external_reference"],
                        "transaction_amount": payment["transaction_amount"],
                        "currency_id": payment["currency_id"],
                        "payment_method_id": payment["payment_method"]["id"],
                        "payment_type_id": payment["payment_method"]["type"],
                        "date_created": payment["date_created"],
                        "date_approved": payment["date_approved"],
                        "payer_email": payment["payer"]["email"],
                    }
                }
            return {
                "success": False,
                "error": "Error al crear la preferencia en Mercado Pago",
                "detail": response
            }
        except Exception as e:
            print(f"Error: {e}")
            return {
                "success": False,
                "error": f"Error {e}",
            }
