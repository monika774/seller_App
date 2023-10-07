from django import forms
from .models import User, Auction

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class AuctionForm(forms.ModelForm):
    class Meta:
        model = Auction
        fields = '__all__'
