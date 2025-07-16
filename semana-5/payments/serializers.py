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
            Product.objects.get(id=value, is_active=True)
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
