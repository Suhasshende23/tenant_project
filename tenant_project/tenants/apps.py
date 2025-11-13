from django.apps import AppConfig
from django.db.utils import OperationalError, ProgrammingError

class TenantsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tenant_project.tenants'
    def ready(self):
        import os
        from tenant_project.tenants.models import Tenant, Domain

        try:
            public_tenant, _ = Tenant.objects.get_or_create(
                schema_name="public",
                defaults={"name": "Public Tenant"}
            )
            public_domain = os.getenv("PUBLIC_DOMAIN", "localhost")

            Domain.objects.get_or_create(
                domain=public_domain,
                tenant=public_tenant,
                defaults={"is_primary": True}
            )

        except (OperationalError, ProgrammingError):
           
            pass