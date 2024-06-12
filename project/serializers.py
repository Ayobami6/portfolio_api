from rest_framework import serializers
from rest_framework.reverse import reverse
from project.models import Project, Tool


class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = ["name"]


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    self_url = serializers.SerializerMethodField()
    tools = ToolSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = (
            "name",
            "description",
            "self_url",
            "link",
            "source_code_link",
            "tools",
        )

    def get_self_url(self, obj):
        request = self.context.get("request")
        return reverse("projects-detail", kwargs={"pk": obj.pk}, request=request)
