from rest_framework import viewsets
from tenant_project.configuration.models import Configuration
from tenant_project.configuration.apis.serializers import ConfigurationSerializer
from rest_framework.permissions import AllowAny
class ConfigurationViewSet(viewsets.ModelViewSet):
    queryset = Configuration.objects.all()
    serializer_class = ConfigurationSerializer
    permission_classes = [AllowAny]  
