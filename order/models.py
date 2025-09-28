from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings
from inventory.models import Listing

# Create your models here.
class Order(models.Model):
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='orders')
    quantity = models.PositiveIntegerField(default=1)
    address = models.TextField()
    status = models.CharField(
        max_length=25,
        choices = (
            ('PENDING', 'Pending'),
            ('CONFIRMED', 'Confirmed'),
            ('SHIPPED', 'Shipped'),
            ('DELIVERED', 'Delivered'),
        ),
        default = "PENDING"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.buyer.username} for {self.listing.title}"