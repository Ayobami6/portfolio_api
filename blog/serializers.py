from rest_framework import serializers
from rest_framework.reverse import reverse

from blog.models import BlogPost


class BlogPostSerializer(serializers.HyperlinkedModelSerializer):
    self_url = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = ("name", "description", "link", "self_url")

    def get_self_url(self, obj):
        request = self.context.get("request")
        return reverse("blog_posts-detail", kwargs={"pk": obj.pk}, request=request)
