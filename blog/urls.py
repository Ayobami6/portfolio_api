from rest_framework import routers
from .views import BlogPostViewSet
from django.urls import path, include

router = routers.DefaultRouter()

router.register(r"blog_posts", BlogPostViewSet, basename="blog_posts")

urlpatterns = [
    path("", include(router.urls)),
]
