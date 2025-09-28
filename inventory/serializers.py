from rest_framework import serializers

from .models import Listing


class ListingSerializer(serializers.ModelSerializer):
    seller = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        fields = (
            "id",
            "title",
            "author",
            "description",
            "quantity",
            "price",
            "created_at",
            "seller",
        )
        model = Listing