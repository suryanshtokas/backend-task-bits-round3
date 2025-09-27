from rest_framework import generics

from .models import Listing
from .serializers import ListingSerializer
from .permissions import IsSellerOrReadOnly


# Create your views here.
class ListingList(generics.ListAPIView):
    permission_classes = (IsSellerOrReadOnly,)
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class ListingDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsSellerOrReadOnly,)
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer