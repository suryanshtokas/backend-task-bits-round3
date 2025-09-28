from rest_framework import generics
from rest_framework import permissions
from .models import Listing
from .serializers import ListingSerializer
from .permissions import IsSellerOrReadOnly
from order.permissions import IsSeller


# Create your views here.
class ListingList(generics.ListAPIView):
    permission_classes = (IsSellerOrReadOnly,)
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class ListingDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsSellerOrReadOnly,)
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class ListingCreate(generics.CreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticated, IsSeller,]

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)