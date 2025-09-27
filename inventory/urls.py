from django.urls import path

from .views import ListingList, ListingDetail

urlpatterns = [
    path("<int:pk>/", ListingDetail.as_view(), name="listing_detail"),
    path("", ListingList.as_view(), name="listing_list"),
]