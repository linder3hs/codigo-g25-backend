from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .views import UserViewSet, verify_email

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
  path('auth/verify-email/', verify_email, name='verify_email'),
  path('', include(router.urls))
]
