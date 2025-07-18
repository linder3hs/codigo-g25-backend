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
from decimal import Decimal
from .services import MercadoPagoService


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
    except Exception as e:
        return Response({
                'success': False,
                'message': 'Datos invalidos',
                'errors': str(e),
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def create_order_from_data(validated_data):
    try:
        # calcular el total de la orden
        total_amount = Decimal('0.00')
        items_data = []

        for item_data in validated_data['items']:
            product = get_object_or_404(Product, id=item_data['product_id'])
            quantity = item_data['quantity']

            # verificar el stack
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
    except Exception:
        return None
