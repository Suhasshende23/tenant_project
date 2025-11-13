from rest_framework import serializers
from tenant_project.consent.models import Consent

class ConsentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consent
        fields = "__all__"
