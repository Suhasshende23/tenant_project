from rest_framework import viewsets, status
from rest_framework.response import Response
from tenant_project.icd.models import ICD
from tenant_project.icd.apis.serializers import ICDPostSerializer, ICDGetSerializer

class ICDViewSet(viewsets.ModelViewSet):
    queryset = ICD.objects.all()

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return ICDPostSerializer
        return ICDGetSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()  # created_date handled automatically
        read_serializer = ICDGetSerializer(instance)
        return Response(read_serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()  # updated_date auto-handled
        read_serializer = ICDGetSerializer(instance)
        return Response(read_serializer.data)
