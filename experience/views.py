from typing import List
from django.shortcuts import render
from rest_framework import viewsets
from utils.exceptions import handle_internal_server_exception
from experience.models import Experience
from experience.serializers import ExperienceSerializer
from rest_framework.response import Response
from utils.response import service_response
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.schemas.openapi import AutoSchema
from drf_yasg.utils import swagger_auto_schema

# Create your views here.


class ExperienceViewSet(viewsets.ModelViewSet):
    """Experience API ViewSet"""

    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

    def list(self, request, *args, **kwargs) -> Response:
        """List all available Work Experience"""
        try:
            experiences: List[Experience] = Experience.objects.all().order_by(
                "-start_date"
            )
            serializer: List[ExperienceSerializer] = self.serializer_class(
                experiences, many=True
            )
            data: List[dict] = serializer.data
            return service_response(
                status="success",
                message="AY Experiences Successfully Fetched",
                data=data,
                status_code=200,
            )

        except Exception:
            return handle_internal_server_exception()

    def retrieve(self, request, *args, **kwargs):
        try:
            experience: Experience = Experience.objects.get(id=kwargs["pk"])
            serializer: ExperienceSerializer = self.serializer_class(experience)
            data: dict = serializer.data
            return service_response(
                status="success",
                message="AY Experience Successfully Fetched",
                data=data,
                status_code=200,
            )
        except Experience.DoesNotExist:
            return service_response(
                status="error", message="Project Not Found", status_code=404
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
