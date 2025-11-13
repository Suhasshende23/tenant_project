from rest_framework import viewsets
from tenant_project.vital.models import Vital
from tenant_project.vital.apis.serializers import VitalCongigurationSerializer


class VitalConfigurationViewSet(viewsets.ModelViewSet):
    queryset = Vital.objects.all()
    serializer_class = VitalCongigurationSerializer


