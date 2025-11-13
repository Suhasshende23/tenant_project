# # tenants/urls.py
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from tenant_project.tenants.views import TenantViewSet
# from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView




# urlpatterns =  [
#     path('api/schema/', SpectacularAPIView.as_view(), name='public-schema'),
#     path('api/docs/', SpectacularSwaggerView.as_view(url_name='public-schema'), name='public-swagger'),
#     path('api/', include('tenant_project.tenants.urls')),  # tenant routes
# ]
