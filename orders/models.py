from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Order(models.Model):
    foydalanuvchi_id = models.IntegerField(default=1)
    buyurtma_sanasi = models.DateTimeField(auto_now_add=True)
    class BuyurtmaHolati(models.TextChoices):
        pending = 'pending','Kutishda'
        shipped = 'shipped','Yetkazilmoqda'
        delivered = 'delivered','Yetkazildi'
    order_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=10,decimal_places=2,default=0)
