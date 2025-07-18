from rest_framework import serializers
from products.models import Product


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
