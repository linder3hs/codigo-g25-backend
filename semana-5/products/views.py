from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import AllowAny

class ProductViewSet(viewsets.ModelViewSet):
    """
    CRUD completo
    """
    queryset = Product.objects.all()
    permission_classes = [AllowAny]
    serializer_class = ProductSerializer
