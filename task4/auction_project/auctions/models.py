# auctions/models.py
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255)
    # Add other user fields as needed
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Auction(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    start_price = models.DecimalField(max_digits=10, decimal_places=2)
    item_name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='auctions')
