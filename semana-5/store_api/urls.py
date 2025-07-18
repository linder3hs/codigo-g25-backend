from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/', include('products.urls')),
    path('api/v1/', include('categories.urls')),
    path('api/v1/',  include('accounts.urls')),
    path('api/v1/payments/', include('payments.urls'))
]
