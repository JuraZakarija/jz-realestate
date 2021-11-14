from django.urls import path, include
from .views import UserProfileView

urlpatterns = [
    path("update_profile/", UserProfileView.as_view(), name="user-profile"),
]
