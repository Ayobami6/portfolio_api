from typing import List
from django.shortcuts import render
from rest_framework import viewsets
from certificate.models import Certificate
from certificate.serializers import CertificateSerializer
from utils.exceptions import handle_internal_server_exception
from utils.response import service_response
from rest_framework.exceptions import MethodNotAllowed
from drf_yasg.utils import swagger_auto_schema

# Create your views here.


class CertificateViewSet(viewsets.ModelViewSet):
    """Certificate view set"""

    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

    def list(self, request, *args, **kwargs):
        """List all certificates"""
        try:
            certs: List[Certificate] = Certificate.objects.all()
            serializer: List[CertificateSerializer] = self.serializer_class(
                certs, many=True
            )
            data: List[dict] = serializer.data
            return service_response(
                status="success",
                message="AY Certificates Fetched Successfully",
                data=data,
                status_code=200,
            )
        except Exception:
            return handle_internal_server_exception()

    def retrieve(self, request, *args, **kwargs):
        """Retrieve a certificate"""
        try:
            certificate: Certificate = Certificate.objects.get(id=kwargs["pk"])
            serializer: CertificateSerializer = self.serializer_class(certificate)
            data: dict = serializer.data
            return service_response(
                status="success",
                message="AY Certificate Fetched Successfully",
                data=data,
                status_code=200,
            )
        except Certificate.DoesNotExist:
            return service_response(
                status="error", message="Certificate Not Found", status_code=404
            )
        except Exception:
            return handle_internal_server_exception()

    @swagger_auto_schema(auto_schema=None)
    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)

    @swagger_auto_schema(auto_schema=None)
    def create(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)

    @swagger_auto_schema(auto_schema=None)
    def update(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)

    @swagger_auto_schema(auto_schema=None)
    def partial_update(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)
