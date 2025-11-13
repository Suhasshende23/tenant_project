from rest_framework import viewsets,parsers
from tenant_project.provider.models import Provider
from tenant_project.provider.apis.serializers import ProviderSerializer
from rest_framework.permissions import AllowAny

class ProviderViewSet(viewsets.ModelViewSet):
    
    queryset = Provider.objects.all().order_by("id")
    serializer_class = ProviderSerializer
    permission_classes = [AllowAny]
    parser_classes = [parsers.MultiPartParser]
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)