from django.urls import path
from .views import create_payment, webhook_notification

urlpatterns = [
    path('create/', create_payment, name='create_payment'),
    path('webhook/', webhook_notification, name='webhook_notification')
]
