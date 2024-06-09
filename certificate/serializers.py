from rest_framework import serializers
from rest_framework.reverse import reverse

from certificate.models import Certificate


class CertificateSerializer(serializers.HyperlinkedModelSerializer):
    self_url = serializers.SerializerMethodField()

    class Meta:
        model = Certificate
        fields = ("name", "description", "cert_file", "self_url")

    def get_self_url(self, obj):
        request = self.context.get("request")
        return reverse("certificates-detail", kwargs={"pk": obj.pk}, request=request)
