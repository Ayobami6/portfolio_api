from django.shortcuts import render
from rest_framework import viewsets
from utils.exceptions import handle_internal_server_exception
from project.models import Project
from project.serializers import ProjectSerializer
from rest_framework.response import Response
from typing import List
from utils.response import service_response
from rest_framework.exceptions import MethodNotAllowed
from drf_yasg.utils import swagger_auto_schema

# Create your views here.


class ProjectViewSet(viewsets.ModelViewSet):
    """Projects API Viewset"""

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def list(self, request, *args, **kwargs) -> Response:
        """List Projects endpoint"""
        try:
            projects: List[Project] = Project.objects.all()
            serializer: List[ProjectSerializer] = self.serializer_class(
                projects, many=True
            )
            data: List[dict] = serializer.data
            return service_response(
                status="success",
                message="AY Projects Fetched Successfully",
                data=data,
                status_code=200,
            )
        except Exception:
            return handle_internal_server_exception()

    def retrieve(self, request, *args, **kwargs):
        """Retrieve a Project"""
        try:
            project: Project = Project.objects.get(id=kwargs["pk"])
            serializer: ProjectSerializer = self.serializer_class(project)
            data: dict = serializer.data
            return service_response(
                status="success",
                message="AY Project Fetched Successfully",
                data=data,
                status_code=200,
            )
        except Project.DoesNotExist:
            return service_response(
                status="error", message="Project Not Found", status_code=404
            )
        except Exception:
            return handle_internal_server_exception()

    # disable unused method endpoints
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
