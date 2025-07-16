from django.db import models

class Order(models.Model):
  STATUS_CHOICES = [
    ('pending', 'Pendiente'),
    ('paid', 'Pagado'),
    ('failed', 'Fallido'),
    ('cancelled', 'Cancelado')
  ]

  order_number = models.CharField(max_length=20, unique=True, blank=True)
  # informacion del cliente
  customer_email = models.EmailField()
  customer_name = models.CharField(max_length=100)
  customer_phone = models.CharField(max_length=13, blank=True)

  # total
  total_amount = models.DecimalField(max_digits=10, decimal_places=2)
  # status
  status = models.CharField(choices=STATUS_CHOICES, max_length=30, default='pending')

  # informacion de mercado pago
  preference_id = models.CharField(max_length=100, blank=True)
  payment_id = models.CharField(max_length=100, blank=True)
  payment_status = models.CharField(max_length=100, blank=True)

  # fechas
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  paid_at = models.DateTimeField(null=True, blank=True)

  class Meta:
      db_table = "orders"
  
  def __str__(self):
     return f"{self.preference_id}"
