from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)

# esta variable debe llamarse asi es un nombre reservador
urlpatterns = [
  path('', include(router.urls))
]
