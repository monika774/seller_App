# auctions/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('users/<int:user_id>/', views.user_detail, name='user_detail'),
    path('users/create/', views.user_create, name='user_create'),
    path('users/<int:user_id>/update/', views.user_update, name='user_update'),
    path('users/<int:user_id>/delete/', views.user_delete, name='user_delete'),

    path('auctions/', views.auction_list, name='auction_list'),
    path('auctions/<int:auction_id>/', views.auction_detail, name='auction_detail'),
    path('auctions/create/', views.auction_create, name='auction_create'),
    path('auctions/<int:auction_id>/update/', views.auction_update, name='auction_update'),
    path('auctions/<int:auction_id>/delete/', views.auction_delete, name='auction_delete'),
]
