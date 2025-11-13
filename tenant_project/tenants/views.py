from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from tenant_project.tenants.serializers import  TenantSerializer
from tenant_project.tenants.models import Tenant
from rest_framework.permissions import AllowAny
class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer  # Now includes domain_name

    permission_classes=[AllowAny]
    # Optional: override create to handle the domain
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tenant = serializer.save()
        return Response({
            "id": tenant.id,
            "schema_name": tenant.schema_name,
            "name": tenant.name,
            "domain_name": request.data.get("domain_name")
        }, status=status.HTTP_201_CREATED)
