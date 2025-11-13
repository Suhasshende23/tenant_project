from rest_framework import viewsets
from tenant_project.flag.models import Flag
from .serializers import FlagSerializer

class FlagViewSet(viewsets.ModelViewSet):
    queryset = Flag.objects.all()
    serializer_class = FlagSerializer
