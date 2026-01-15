from django.db import models
from django.contrib.auth.models import User,AbstractUser
# Create your models here.
class User(AbstractUser):
    ism = models.CharField(max_length=25)
    class Role(models.TextChoices):
        admin = "admin","Admin"
        customer = "customer","Haridor"
    
    def __str__(self):
        return self.ism
    
