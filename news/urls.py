from django.urls import path
from .views import BlogPostListView, BlogPostDetailView


urlpatterns = [
    path("", BlogPostListView.as_view(), name="news"),
    path("<slug:slug>/", BlogPostDetailView.as_view(), name="news-detail"),
]
