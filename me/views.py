from django.shortcuts import render
from rest_framework.views import APIView

from me.models import ME, Education, Interest, ProgrammingLanguage, Technologies
from me.serializers import MESerializer
from utils.exceptions import handle_internal_server_exception
from utils.response import service_response
from django.contrib.sites.shortcuts import get_current_site
from django.db.models import Prefetch

# Create your views here.


class RootPage(APIView):
    """Ayobami Alaran API Portfolio"""

    def get(self, request, format=None):
        try:
            data: dict = dict()
            current_site = get_current_site(request)
            site_domain = current_site.domain
            data["site"] = site_domain
            return service_response(
                status="success",
                message="Welcome to Ayobami Alaran API Portfolio",
                data=data,
                status_code=200,
            )
        except Exception:
            return handle_internal_server_exception()


class ProfileAPIView(APIView):
    """My Profile details API view"""

    serializer_class = MESerializer

    def get(self, request, *args, **kwargs):
        try:
            profile = (
                ME.objects.prefetch_related(
                    Prefetch(
                        "plangs", queryset=ProgrammingLanguage.objects.only("name")
                    ),
                    Prefetch(
                        "technologies", queryset=Technologies.objects.only("name")
                    ),
                    Prefetch("educations", queryset=Education.objects.only("name")),
                    Prefetch("interests", queryset=Interest.objects.only("name")),
                )
                .all()
                .first()
            )
            data = {
                "name": profile.name,
                "email": profile.email,
                "phone_number": str(profile.phone_number),
                "technologies": [tech.name for tech in profile.technologies.all()],
                "programming_languages": [plang.name for plang in profile.plangs.all()],
                "educations": [edu.name for edu in profile.educations.all()],
                "interests": [interest.name for interest in profile.interests.all()],
                "pronouns": profile.pronouns,
                "current_focus": profile.current_focus,
                "fun_fact": profile.fun_fact,
            }
            return service_response(
                status="success",
                message="Thanks for Checking Out!",
                data=data,
                status_code=200,
            )
        except Exception:
            return handle_internal_server_exception()
