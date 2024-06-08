from django.urls import include, path
from rest_framework import routers

from project.views import ProjectViewSet

router = routers.DefaultRouter()

router.register(
    r"projects",
    ProjectViewSet,
    basename="projects",
)

urlpatterns = [
    path("", include(router.urls)),
]
