

# Register your models here.
# auctions/admin.py
from django.contrib import admin
from .models import User, Auction

admin.site.register(User)
admin.site.register(Auction)
