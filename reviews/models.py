from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)

    def str(self):
        return self.name
    
class ProductReview(models.Model):
    class Rating(models.TextChoices):
        bir = "1", "- Juda yomon"
        ikki = "2", "- Yomon"
        uch = "3", "- O'rtacha"
        tort = "4", "- Yaxshi"
        besh = "5", "- A'lo"
        
    user = models.ForeignKey(Product,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)