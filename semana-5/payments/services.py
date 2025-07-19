import mercadopago
from django.conf import settings
import json

class MercadoPagoService:
    """
    Servicio para implementar pasarelas de pago en mi aplicación
    """

    def __init__(self):
        self.sdk = mercadopago.SDK(settings.MERCADOPAGO_ACCESS_TOKEN)

    def create_preference(self, items, order_data):
        """
        Preferencia de mercadopago
        """
        try:
            # 🔍 DEBUG: Validar items
            print("🛒 Items recibidos:")
            for i, item in enumerate(items):
                print(f"  Item {i+1}: {json.dumps(item, indent=2, default=str)}")
                
                # Validaciones críticas
                if not item.get('currency_id'):
                    print(f"❌ ERROR: Item {i+1} sin currency_id")
                if not item.get('title'):
                    print(f"❌ ERROR: Item {i+1} sin título")
                if not item.get('unit_price') or item.get('unit_price') <= 0:
                    print(f"❌ ERROR: Item {i+1} precio inválido: {item.get('unit_price')}")

            # Limpiar y validar teléfono
            phone_number = str(order_data.get('customer_phone', '')).strip()
            phone_number = phone_number.replace('+51', '').replace(' ', '').replace('-', '')
            
            # Construir datos del pagador de forma segura
            payer_data = {
                "name": order_data.get('customer_name', '').strip(),
                "email": order_data.get('customer_email', '').strip()
            }
            
            # Solo agregar teléfono si es válido
            if phone_number and len(phone_number) >= 9:
                payer_data["phone"] = {
                    "area_code": "51",
                    "number": phone_number
                }

            preference_data = {
                "items": items,
                "external_reference": str(order_data.get('order_id')),
                "payer": payer_data,
                "payment_methods": {
                    "excluded_payment_methods": [],
                    "excluded_payment_types": [],
                    "installments": 12
                }
            }

            # Solo agregar notification_url si es una URL pública
            base_url = getattr(settings, 'BASE_URL', '')
            if base_url and (base_url.startswith('https://') or 'ngrok' in base_url):
                preference_data["notification_url"] = f"{base_url}/api/v1/payments/webhook/"
                print(f"✅ Notification URL agregada: {preference_data['notification_url']}")
            else:
                print(f"⚠️ Notification URL omitida (no es pública): {base_url}")

            # 🔍 DEBUG: Mostrar preference_data completa
            print("📋 Preference data enviada:")
            print(json.dumps(preference_data, indent=2, default=str))

            response = self.sdk.preference().create(preference_data)
            
            # 🔍 DEBUG: Mostrar respuesta
            print("📥 Respuesta de MercadoPago:")
            print(f"Status: {response.get('status')}")
            print(json.dumps(response, indent=2, default=str))

            if response["status"] == 201:
                preference = response["response"]  # ✅ CORRECTO

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
            print(f"💥 Error en create_preference: {e}")
            import traceback
            traceback.print_exc()
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
            
            print(f"🔍 Payment response: {json.dumps(response, indent=2, default=str)}")
            
            if response["status"] == 200:
                # ✅ CORREGIDO: era response["payment"], debe ser response["response"]
                payment = response["response"]
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
                "error": "Error al obtener información del pago",
                "detail": response
            }
        except Exception as e:
            print(f"💥 Error en get_payment_info: {e}")
            import traceback
            traceback.print_exc()
            return {
                "success": False,
                "error": f"Error {e}",
            }

    def verify_configuration(self):
        """
        Verificar que la configuración de MercadoPago sea correcta
        """
        try:
            print("🔧 Verificando configuración...")
            
            # Verificar access token
            token = getattr(settings, 'MERCADOPAGO_ACCESS_TOKEN', None)
            if not token:
                print("❌ MERCADOPAGO_ACCESS_TOKEN no configurado")
                return False
            
            if not token.startswith('TEST-'):
                print("❌ Access token no es de prueba (debe empezar con TEST-)")
                return False
            
            print(f"✅ Access token válido: {token[:15]}...")
            
            # Verificar conexión con MercadoPago
            response = self.sdk.user().get()
            if response['status'] == 200:
                user = response['response']
                print(f"✅ Conexión exitosa con MercadoPago")
                print(f"   User ID: {user.get('id')}")
                print(f"   Email: {user.get('email')}")
                print(f"   Country: {user.get('country_id')}")
                return True
            else:
                print(f"❌ Error conectando con MercadoPago: {response}")
                return False
                
        except Exception as e:
            print(f"❌ Error verificando configuración: {e}")
            return False
