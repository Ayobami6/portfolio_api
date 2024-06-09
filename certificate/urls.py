from rest_framework import routers
from django.urls import path, include

from certificate.views import CertificateViewSet


router = routers.DefaultRouter()

router.register(r"certificates", CertificateViewSet, basename="certificates")


urlpatterns = [
    path("", include(router.urls)),
]
