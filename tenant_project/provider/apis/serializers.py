from rest_framework import serializers
from tenant_project.provider.models import Provider

class ProviderSerializer(serializers.ModelSerializer):
    time_zone = serializers.CharField()
    image = serializers.FileField(required=True)
    image_url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Provider
        fields = "__all__"
    
    def get_image_url(self, obj):
        request = self.context.get("request")
        if obj.image and hasattr(obj.image, "url"):
            return request.build_absolute_uri(obj.image.url)
        return None    