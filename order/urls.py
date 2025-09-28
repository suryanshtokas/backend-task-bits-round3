from django.urls import path
from .views import OrderCreateView, BuyerOrderView, SellerOrderView


urlpatterns = [
    path('create/', OrderCreateView.as_view(), name="order_create"),
    path('my-orders/', BuyerOrderView.as_view(), name="buyer-orders"),
    path('seller-orders/', SellerOrderView.as_view(), name='seller-orders'),
]