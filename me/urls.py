from .views import RootPage, ProfileAPIView
from django.urls import path, include

urlpatterns = [
    path("root", RootPage.as_view(), name="root"),
    path("me", ProfileAPIView.as_view(), name="me")
]
