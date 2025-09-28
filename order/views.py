from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from .models import Order
from.serializers import OrderSerializer
from .permissions import IsSeller, IsBuyer


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated, IsBuyer,]

    def perform_create(self, serializer):
        listing = serializer.validated_data['listing']

        if listing.quantity < serializer.validated_data['quantity']:
            raise ValidationError("Listing doesen't have enough stock")
        
        listing.quantity -= serializer.validated_data["quantity"]
        listing.save()
        serializer.save(buyer=self.request.user)


class BuyerOrderView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated, IsBuyer, ]

    def get_queryset(self):
        return Order.objects.filter(buyer=self.request.user)
    

class SellerOrderView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated, IsSeller, ]

    def get_queryset(self):
        return Order.objects.filter(listing__seller=self.request.user)