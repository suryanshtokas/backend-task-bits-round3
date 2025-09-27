from rest_framework import serializers

from .models import Listing


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "title",
            "author",
            "description",
            "created_at",
            "seller",
        )
        model = Listing