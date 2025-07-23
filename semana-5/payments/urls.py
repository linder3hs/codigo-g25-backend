from django.urls import path
from .views import create_payment, webhook_notification, get_payment_info

urlpatterns = [
    path('create/', create_payment, name='create_payment'),
    path('webhook/', webhook_notification, name='webhook_notification'),
    path('info/<str:payment_id>', get_payment_info, name='get_payment_info')
]
