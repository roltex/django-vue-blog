from django.urls import path
from .views import BlogListAPIView, BlogDetailAPIView

urlpatterns = [
    path('blogs/', BlogListAPIView.as_view(), name='blog-list'),  # List all blogs
    path('blogs/<int:pk>/', BlogDetailAPIView.as_view(), name='blog-detail'),  # Retrieve a single blog
]
