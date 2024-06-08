from django.urls import reverse, path, include
from rest_framework import routers
from .views import ExperienceViewSet

router = routers.DefaultRouter()

router.register(r"experiences", ExperienceViewSet, basename="experiences")

urlpatterns = [
    path("", include(router.urls)),
]
