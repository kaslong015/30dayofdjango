from imp import create_dynamic
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class Order(models.Model):

    SIZES = (
        ('SMALL', 'Small'),
        ('MEDIUM', 'Medium'),
        ('LARGE', 'Large'),
        ('EXTRA_LARGE', 'Extra Large'),
    )

    ORDER_STATUS = (
        ('PENDING', 'Pending'),
        ('IN_TRANSIT', 'inTransit'),
        ('DELIVERED', 'Delivered'),
    )

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    size = models.CharField(max_length=100, choices=SIZES,default=SIZES[0][0])
    order_status = models.CharField(max_length=100, choices=ORDER_STATUS,default=ORDER_STATUS[0][0])
    quantity = models.IntegerField() 
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer.username
