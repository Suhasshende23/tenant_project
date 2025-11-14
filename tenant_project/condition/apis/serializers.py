from rest_framework import serializers
from tenant_project.condition.models import Condition

class ConditionPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = ["name", "description", "icd"]  

class ConditionGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = ["id", "name", "description", "icd", "created_date"]  
        read_only_fields = ["created_date"]
