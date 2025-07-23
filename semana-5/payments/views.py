from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from products.models import Product
from .models import Order, OrderItem
from .serializers import (
  CreateOrderSerializer,
  OrderResponseSerializer,
  PaymentLinkSerializer,
  PaymentStatusSerializer
)
import traceback
import sys
from django.conf import settings
from decimal import Decimal
from .services import MercadoPagoService
from services.email_service import EmailService


@api_view(['POST'])
@permission_classes([AllowAny])
def create_payment(request):
    """
    Endpoint para poder crear un nuevo pago
    /api/payments/create/
    """
    try:
        # Validar data de entrada
        serializer = CreateOrderSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({
                'success': False,
                'message': 'Datos invalidos',
                'errors': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        
        validated_data = serializer.validated_data

        # crear la orden
        order = create_order_from_data(validated_data)

        if not order:
            return Response({
                'success': False,
                'message': 'Error al crear la orden',
            }, status=status.HTTP_400_BAD_REQUEST)

        mercadopago_service = MercadoPagoService()
        items = prepare_mercadopago_items(order)

        order_data = {
            'order_id': order.id,
            'customer_email': order.customer_email,
            'customer_name': order.customer_name,
            'customer_phone': order.customer_phone
        }

        mercadopago_response = mercadopago_service.create_preference(items, order_data)

        print(mercadopago_response)

        if mercadopago_response.get('success'):
            order.preference_id = mercadopago_response.get('preference_id')
            order.save()

            order_serializer = OrderResponseSerializer(order)

            # pasa que tenemos 2 url de pago
            payment_url = (
                mercadopago_response.get('sandbox_init_point')
                if settings.MERCADOPAGO_SANDBOX
                else mercadopago_response.get('init_point')
            )

            return Response({
                'success': True,
                'message': 'Orden creada exitosamente',
                'order': order_serializer.data,
                'payment_link': payment_url,
                'preference_id': mercadopago_response.get('preference_id')
            }, status=status.HTTP_201_CREATED)
        else:
            # Manejar el caso cuando MercadoPago falla
            return Response({
                'success': False,
                'message': 'Error al crear preferencia de pago',
                'errors': mercadopago_response.get('error', 'Error desconocido')
            }, status=status.HTTP_400_BAD_REQUEST)
            
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        
        # Extract the last frame information (where the error occurred)
        tb_info = traceback.extract_tb(exc_traceback)[-1]
        
        # Get the filename and line number
        filename = tb_info.filename
        line_number = tb_info.lineno
        
        print(f"An error occurred:")
        print(f"  Type: {type(e).__name__}")
        print(f"  Message: {e}")
        print(f"  File: {filename}")
        print(f"  Line: {line_number}")

        return Response({
            'success': False,
            'message': 'Error en el servidor',
            'errors': str(e),
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def create_order_from_data(validated_data):
    try:
        # calcular el total de la orden
        total_amount = Decimal('0.00')
        items_data = []

        for item_data in validated_data['items']:
            print("---items_data----")
            print(item_data)
            product = get_object_or_404(Product, id=item_data['product_id'])
            quantity = item_data['quantity']

            # verificar el stock
            if product.stock < quantity:
                return None

            unit_price = product.price
            total_price = unit_price * quantity
            total_amount += total_price

            items_data.append({
                'product': product,
                'quantity': quantity,
                'unit_price': unit_price,
                'total_price': total_price
            })

        # crear la orden
        order = Order.objects.create(
            customer_email=validated_data['customer_email'],
            customer_name=validated_data['customer_name'],
            customer_phone=validated_data.get('customer_phone', ''),
            total_amount=total_amount
        )

        # crear los items de la orden
        for item_data in items_data:
            OrderItem.objects.create(
                order=order,
                product=item_data['product'],
                quantity=item_data['quantity'],
                unit_price=item_data['unit_price']
            )

            # reducir el stock
            product = item_data['product']
            product.stock -= item_data['quantity']
            product.save()
        return order
    except Exception as e:
        print(f"Error al crear la orden: {e}")
        exc_type, exc_value, exc_traceback = sys.exc_info()

        # Extract the last frame information (where the error occurred)
        tb_info = traceback.extract_tb(exc_traceback)[-1]

        # Get the filename and line number
        filename = tb_info.filename
        line_number = tb_info.lineno

        print(f"An error occurred:")
        print(f"  Type: {type(e).__name__}")
        print(f"  Message: {e}")
        print(f"  File: {filename}")
        print(f"  Line: {line_number}")

        return None


def prepare_mercadopago_items(order):
    """
    Preparar la data para mercadopago
    """
    items = []

    for order_item in order.items.all():
        print('----order_item---')
        print(order_item)
        items.append(order_item.product.to_mercadopago_item(order_item.quantity))

    return items


@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def webhook_notification(request):
    """
    Webhook para recibir notificaciones de mercadopago
    """
    print("========INFORMACION DEL WEBHOOK========")
    mercadopago_data = request.data
    notification_type = mercadopago_data.get('type')
    print("request.data")
    print(mercadopago_data)

    print("notification_type")
    print(notification_type)

    if notification_type == 'payment':
        payment_id = mercadopago_data.get('data').get('id')

        if payment_id:
            result = proccess_payment_notifacation(payment_id)
            print("-----RESULT DATA-------")
            print(result)
            print("------END DATA------")
            return Response({
                'data': result
            })

    return Response({
            'error': 'Datos invaliddos'
        })


def proccess_payment_notifacation(payment_id):
    try:
        mercadopago_service = MercadoPagoService()
        payment_info = mercadopago_service.get_payment_info(payment_id)

        print("-----payment_info-----")
        print(payment_info)
        print("*"*50)

        if not payment_info.get('success'):
            return "Error al procesar el pago"

        payment_data = payment_info.get('payment')
       
        external_reference = payment_data.get('external_reference')
        print("-----payment_data-----")
        print("-----payment_data-----")
        print(payment_data)
        print("*"*50)
        print(external_reference)
        print("*"*50)

        if not external_reference:
            return "Sin external reference"

        order = Order.objects.get(id=int(external_reference))

        if not order:
            return "Orden no encontrada"

        order.payment_id = payment_data['id']
        order.payment_status = payment_data['status']

        email_service = EmailService()

        payment_data_to_email = {
            "payment": {
                "payer_email": "linderhassinger@helloiconic.com",
                "status": payment_data.get('status'),
                "order_items": payment_data.get('items'),
                "currency_id": payment_data.get("currency_id"),
                "transaction_amount": payment_data.get("transaction_amount"),
                "id": payment_data.get("id"),
                "external_reference": payment_data.get("external_reference"),
                "payment_method_id": payment_data.get("payment_method_id"),
                "payment_type_id": payment_data.get("payment_type_id"),
                "date_created": payment_data.get("date_created"),
                "date_approved": payment_data.get("date_approved")
            }
        }

        if payment_data['status'] == "approved":
            # send email
            order.status = 'paid'
            order.paid_at = payment_data.get('date_approved')

            email_service.send_verification_payment("linder.hassinger@helloiconic.com", payment_data_to_email)
        elif payment_data['status'] == 'pending':
            order.status = 'pending'
        elif payment_data['status'] == 'rejected':
            order.status = 'failed'

            # restaurar el stock
            restore_order_stock(order)
        order.save()

        return f"Pago proecesado {order.order_number} - {order.status}"
    except Exception as e:
        return f"Error: {e}"


def restore_order_stock(order):
    """
    Restaurar el stock
    """
    try:
        for item in order.items.all():
            product = item.product
            product.stack += item.quantity
            product.save()
    except Exception as e:
        print(f"Error {e}")


@api_view(['GET'])
@permission_classes([AllowAny])
def get_payment_info(request, payment_id):
    """
    Obtener el detalle del pago
    """
    try:
        mercado_pago_service = MercadoPagoService()
        payment_info_response = mercado_pago_service.get_payment_info(payment_id)

        if not payment_info_response["success"]:
            return Response({
                'success': False,
                'message': 'Pago no encontrado',
            }, status=status.HTTP_400_BAD_REQUEST)
        
        payment_data = payment_info_response.get('payment')

        response_data = {
            'success': True,
            'payment': payment_data
        }

        external_reference = payment_data.get('external_reference')

        if external_reference:
            try:
                order = Order.objects.get(id=int(external_reference))
                order_serializer = OrderResponseSerializer(order)

                response_data['order'] = order_serializer.data
            except Order.DoesNotExist:
                response_data['order'] = {
                    'external_reference': external_reference,
                    'found': False,
                    'message': 'Order no encontrada'
                }
        else:
            print("External reference not found")

        return Response(response_data)
    except Exception as e:
        return Response({
            'success': False,
            'message': 'Error en el servidor',
            'errors': str(e),
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
