from rest_framework import viewsets, status
from rest_framework.response import Response
from tenant_project.template.models import Template
from tenant_project.template.apis.serializers import TemplatePostSerializer, TemplateGetSerializer

class TemplateViewSet(viewsets.ModelViewSet):
    queryset = Template.objects.all()

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return TemplatePostSerializer
        return TemplateGetSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()  
        readserializer = TemplateGetSerializer(instance)
        return Response(readserializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        readserializer = TemplateGetSerializer(instance)
        return Response(readserializer.data)
