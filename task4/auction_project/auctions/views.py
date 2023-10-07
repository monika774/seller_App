

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import User, Auction
from .forms import UserForm, AuctionForm
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer, AuctionSerializer

# Views for HTML rendering

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'user_detail.html', {'user': user})

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'user_create.html', {'form': form})

def user_update(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'user_update.html', {'form': form, 'user': user})

def user_delete(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'user_delete.html', {'user': user})

def auction_list(request):
    auctions = Auction.objects.all()
    return render(request, 'auction_list.html', {'auctions': auctions})

def auction_detail(request, auction_id):
    auction = get_object_or_404(Auction, id=auction_id)
    return render(request, 'auction_detail.html', {'auction': auction})

def auction_create(request):
    if request.method == 'POST':
        form = AuctionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('auction_list')
    else:
        form = AuctionForm()
    return render(request, 'auction_create.html', {'form': form})

def auction_update(request, auction_id):
    auction = get_object_or_404(Auction, id=auction_id)
    if request.method == 'POST':
        form = AuctionForm(request.POST, instance=auction)
        if form.is_valid():
            form.save()
            return redirect('auction_list')
    else:
        form = AuctionForm(instance=auction)
    return render(request, 'auction_update.html', {'form': form, 'auction': auction})

def auction_delete(request, auction_id):
    auction = get_object_or_404(Auction, id=auction_id)
    if request.method == 'POST':
        auction.delete()
        return redirect('auction_list')
    return render(request, 'auction_delete.html', {'auction': auction})

# Views for REST API (using Django Rest Framework)

@api_view(['GET', 'POST'])
def api_user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def api_user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def api_auction_list(request):
    if request.method == 'GET':
        auctions = Auction.objects.all()
        serializer = AuctionSerializer(auctions, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AuctionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def api_auction_detail(request, auction_id):
    auction = get_object_or_404(Auction, id=auction_id)
    if request.method == 'GET':
        serializer = AuctionSerializer(auction)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AuctionSerializer(auction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        auction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
