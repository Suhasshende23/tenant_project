from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

# from tenant_project.users.api.views import UserViewSet
from tenant_project.tenants.views import TenantViewSet
from tenant_project.provider.apis.views import ProviderViewSet

from tenant_project.configuration.apis.views import ConfigurationViewSet
from tenant_project.consent.apis.views import ConsentViewSet
from tenant_project.vital.apis.views import VitalConfigurationViewSet
from tenant_project.flag.apis.views import FlagViewSet
router = DefaultRouter() if settings.DEBUG else SimpleRouter()

# router.register("users", UserViewSet)
router.register(r"tenants", TenantViewSet, basename='tenants')
router.register(r'providers', ProviderViewSet, basename='provider')
router.register(r'configurations', ConfigurationViewSet,basename='configuration')
router.register(r'consents', ConsentViewSet,basename='consent')
router.register(r'vitals', VitalConfigurationViewSet,basename='vital')
router.register(r'flags', FlagViewSet, basename='flag')
app_name = "api"
urlpatterns = router.urls
