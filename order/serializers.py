from rest_framework import serializers

from .models import Order

from inventory.models import Listing


class OrderSerializer(serializers.ModelSerializer):
    buyer = serializers.SlugRelatedField(read_only=True, slug_field="username")
    listing = serializers.PrimaryKeyRelatedField(queryset=Listing.objects.all())
    listing_title = serializers.CharField(source='listing.title', read_only=True)

    class Meta:
        model = Order
        fields = "__all__"