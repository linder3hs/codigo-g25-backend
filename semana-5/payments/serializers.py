from rest_framework import serializers
from products.models import Product
from .models import Order

class CreateOrderItemSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)

    def validate_product_id(self, value):
        """
        Valida si el producto existe y esta activo
        """
        try:
            product = Product.objects.get(id=value, is_active=True)
            if not product:
                return serializers.ValidationError("Producto no encontrado")
            return value
        except Exception as e:
            return serializers.ValidationError("Producto no encontrado")

    def validate(self, data):
        """
        Validar el Stock del product
        """
        try:
            product = Product.objects.get(id=data['product_id'], is_active=True)

            if product.stock < data['quantity']:
                return serializers.ValidationError("Producto sin stock")
            return data
        except Exception:
            return serializers.ValidationError("Producto sin stock")

class CreateOrderSerializer(serializers.Serializer):
    """
    Serializer principal para crear la orden
    """
    customer_email = serializers.EmailField()
    customer_name = serializers.CharField(max_length=100)
    customer_phone = serializers.CharField(max_length=20, required=False, allow_blank=True)
    items = CreateOrderItemSerializer(many=True)

    def validate_items(self, value):
        if not value:
            raise serializers.ValidationError("La orden debe tener al menos un producto.")
        return value


class OrderResponseSerializer(serializers.ModelSerializer):
    """
    Serializer para mostrar el detalle de la orden
    """
    items = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'order_number', 'customer_email', 'customer_name',
                  'total_amount', 'status', 'payment_status', 'created_at',
                  'items']

    def get_items(self, obj):
        """
        Items de la orden
        """
        return [
            {
                "product_name": item.product.name,
                "quantity": item.quantity,
                'unit_price': str(item.unit_price),
                'total_price': str(item.total_price)
            }
            for item in obj.items.all()
        ]


class PaymentLinkSerializer(serializers.Serializer):
    """
    Serializer para la respuesta con link de pago
    """
    order_id = serializers.IntegerField()
    preference_id = serializers.CharField()
    payment_url = serializers.URLField()
    sandbox_payment_url = serializers.URLField()


class PaymentStatusSerializer(serializers.Serializer):
    """
    Serializer para consultar el estado de pago
    """
    order_id = serializers.IntegerField()
    order_status = serializers.CharField()
    payment_status = serializers.CharField()
    payment_id = serializers.CharField(required=False)
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
