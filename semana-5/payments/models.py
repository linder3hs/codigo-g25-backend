from django.db import models
from products.models import Product
from datetime import datetime

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
  
  def save(self, *args, **kwargs):
      if not self.order_number:
          self.order_number = self.generate_order_number()
      super().save(*args, **kwargs)

  def generate_order_number(self):
      """
      Formato MP-YYYYMMDD-XXXX
      """
      today = datetime.now().strftime('%Y%m%d')
      last_order = Order.objects.filter(order_number__startswith=f'MP-{today}').order_by('-order_number').first()

      if last_order:
          last_num = int(last_order.order_number.split('-')[-1])
          next_num = last_num + 1
      else:
          next_num = 1

      return f'MP-{today}-{next_num:04d}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'order_items'
    
    def __str__(self):
       return f"{self.product.name} - {self.order.order_number}"
  
    def save(self, *args, **kwargs):
        """Calcular el total unit_pice * quantity"""
        self.total_price = self.quantity * self.unit_price
        return super().save(*args, **kwargs)
