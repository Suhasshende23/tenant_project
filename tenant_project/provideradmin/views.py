from rest_framework import viewsets, status
from rest_framework.response import Response
from tenant_project.provideradmin.models import ProviderAdmin
from tenant_project.provideradmin.serializers import ProviderAdminPostSerializer, ProviderAdminGetSerializer

class ProviderAdminViewSet(viewsets.ModelViewSet):
    queryset = ProviderAdmin.objects.select_related("user")

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return ProviderAdminPostSerializer
        return ProviderAdminGetSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        read_serializer = ProviderAdminGetSerializer(instance)
        return Response(read_serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        read_serializer = ProviderAdminGetSerializer(instance)
        return Response(read_serializer.data)
