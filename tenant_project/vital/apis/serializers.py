from rest_framework import serializers
from tenant_project.vital.models import Vital


class VitalCongigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vital
        fields = "__all__"


