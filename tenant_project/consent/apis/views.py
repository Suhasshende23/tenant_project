from rest_framework import viewsets
from tenant_project.consent.models import Consent

from .serializers import ConsentSerializer

class ConsentViewSet(viewsets.ModelViewSet):
    queryset = Consent.objects.all()
    serializer_class = ConsentSerializer
