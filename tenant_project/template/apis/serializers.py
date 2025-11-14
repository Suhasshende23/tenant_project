from rest_framework import serializers
from tenant_project.template.models import Template


class TemplatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = ["name", "template_type", "subject", "description"]


class TemplateGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = ["id", "name", "template_type", "subject", "description", "created_date"]
        read_only_fields = ["created_date"]
