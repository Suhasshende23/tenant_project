from rest_framework import serializers
from tenant_project.flag.models import Flag

class FlagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flag
        fields = "__all__"
