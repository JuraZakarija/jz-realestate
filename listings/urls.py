from django.urls import path
from .views import (
    ListingListView,
    ListingDetailView,
    ListingCreateView,
    ListingUpdateView,
    ListingDeleteView,
    UserListingsView,
)

urlpatterns = [
    path("", ListingListView.as_view(), name="listings"),
    path("<str:username>", UserListingsView.as_view(), name="user-listings"),
    path("create/", ListingCreateView.as_view(), name="listing-create"),
    path("<slug:slug>/", ListingDetailView.as_view(), name="listing-detail"),
    path(
        "<slug:slug>/update_listing/",
        ListingUpdateView.as_view(),
        name="listing-update",
    ),
    path(
        "<slug:slug>/delete_listing/",
        ListingDeleteView.as_view(),
        name="listing-delete",
    ),
]
