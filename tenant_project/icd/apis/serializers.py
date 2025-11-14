from rest_framework import serializers
from tenant_project.icd.models import ICD

class ICDPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ICD
        fields = ["title", "code", "condition"]  


class ICDGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ICD
        fields = "__all__" 
        read_only_fields = ["created_date", "updated_date"] 
