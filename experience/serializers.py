from rest_framework import serializers
from rest_framework.reverse import reverse
from experience.models import Experience


class ExperienceSerializer(serializers.HyperlinkedModelSerializer):
    self_url = serializers.SerializerMethodField()

    class Meta:
        model = Experience
        fields = (
            "self_url",
            "title",
            "company",
            "start_date",
            "end_date",
            "location",
            "is_current",
        )

    def get_self_url(self, obj):
        request = self.context.get("request")
        return reverse("experiences-detail", kwargs={"pk": obj.pk}, request=request)
