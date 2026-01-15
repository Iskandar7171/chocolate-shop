from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ChocolateProduct(models.Model):
    nomi = models.CharField(max_length=25)
    tavsifi = models.TextField(blank=True,null=True)
    narxi = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    miqdori = models.IntegerField(default=0)
    class MaxsulotTuri(models.TextChoices):
        dark = "dark","Qora"
        milk = "milk","Sut"
        white = "white","Oq"
  
    def __str__(self):
        return f"{self.nomi} | {self.tavsifi} "
    
class Category(models.Model):
    nomi = models.CharField(max_length=25)
    tavsifi = models.TextField(blank=True,null=True)
    
    def __str__(self):
        return f"{self.nomi} | {self.tavsifi} "
        