from rest_framework import viewsets
from tenant_project.condition.models import Condition
from tenant_project.condition.apis.serializers import ConditionPostSerializer, ConditionGetSerializer

class ConditionViewSet(viewsets.ModelViewSet):
    queryset = Condition.objects.all()

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return ConditionPostSerializer
        return ConditionGetSerializer
