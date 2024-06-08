from typing import List
from django.shortcuts import render
from rest_framework import viewsets

from blog.models import BlogPost
from blog.serializers import BlogPostSerializer
from utils.exceptions import handle_internal_server_exception
from utils.response import service_response
from rest_framework.exceptions import MethodNotAllowed
from drf_yasg.utils import swagger_auto_schema

# Create your views here.


class BlogPostViewSet(viewsets.ModelViewSet):
    """Blog post view set"""

    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def list(self, request, *args, **kwargs):
        """List endpoint for Blog Post API View Set"""
        try:
            posts: List[BlogPost] = BlogPost.objects.all()
            serializer: List[BlogPostSerializer] = BlogPostSerializer(posts, many=True)
            data: List[dict] = serializer.data
            return service_response(
                status="success",
                message="Blog Posts Fetched Successfully",
                data=data,
            )
        except Exception:
            return handle_internal_server_exception()

    def retrieve(self, request, *args, **kwargs):
        """Retrieve a Blog Post"""
        try:
            post: BlogPost = BlogPost.objects.get(id=kwargs["pk"])
            serializer: BlogPostSerializer = self.serializer_class(post)
            data: dict = serializer.data
            return service_response(
                status="success",
                message="Blog Post Fetched Successfully",
                data=data,
                status_code=200,
            )
        except BlogPost.DoesNotExist:
            return service_response(
                status="error", message="Blog Post Not Found", status_code=404
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
