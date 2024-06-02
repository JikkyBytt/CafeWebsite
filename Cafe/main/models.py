from django.db import models
from django.contrib.auth.models import User

class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE)
    item = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
   
    def __str__(self):
        return f"{self.item} - ${self.price}"
        
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_items = models.TextField()  # Store ordered items and quantities as JSON or serialized text
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)