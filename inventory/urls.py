from django.urls import path

from .views import ListingList, ListingDetail, ListingCreate

urlpatterns = [
    path("<int:pk>/", ListingDetail.as_view(), name="listing_detail"),
    path("", ListingList.as_view(), name="listing_list"),
    path("create/", ListingCreate.as_view(), name="listing_create"),
]