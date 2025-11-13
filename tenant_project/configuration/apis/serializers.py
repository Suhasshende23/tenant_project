from rest_framework import serializers
from tenant_project.configuration.models import Configuration

class ConfigurationSerializer(serializers.ModelSerializer):
    time_zone = serializers.CharField() 

    class Meta:
        model = Configuration
        fields = "__all__"
