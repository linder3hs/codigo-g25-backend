from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .views import UserViewSet, verify_email, resend_verification

router = DefaultRouter()
router.register(r'users', UserViewSet)

# auth/resend-verification/

urlpatterns = [
  path('auth/verify-email/', verify_email, name='verify_email'),
  path('auth/resend-verification', resend_verification, name='resend_verification'),
  path('', include(router.urls))
]
