from rest_framework import serializers
from tenant_project.tenants.models import Tenant, Domain

class TenantSerializer(serializers.ModelSerializer):
    # Add domain_name as a write-only field for create/update
    domain_name = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Tenant
        fields = ['id', 'name', 'schema_name', 'domain_name']

    def create(self, validated_data):
        # Pop domain_name from validated_data
        domain_name = validated_data.pop('domain_name')
        # Create Client
        tenant = Tenant.objects.create(**validated_data)
        # Create Domain
        Domain.objects.create(domain=domain_name, tenant=tenant, is_primary=True)
        return tenant
