from rest_framework import serializers

from me.models import Technologies, ME, Education, Interest, ProgrammingLanguage


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technologies
        fields = ["name"]


class ProgrammingLanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProgrammingLanguage
        fields = ["name"]


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ["name"]


class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = ["name"]


class MESerializer(serializers.ModelSerializer):
    technologies = TechnologySerializer(many=True)
    plangs = ProgrammingLanguageSerializer(many=True)
    educations = EducationSerializer(many=True)
    interests = InterestSerializer(many=True)

    class Meta:
        model = ME
        fields = (
            "name",
            "email",
            "phone_number",
            "technologies",
            "plangs",
            "educations",
            "interests",
            "pronouns",
            "current_focus",
            "fun_fact",
        )
