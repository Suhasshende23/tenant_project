from rest_framework import serializers
from django.contrib.auth import get_user_model
from tenant_project.provideradmin.models import ProviderAdmin

User = get_user_model()


class ProviderAdminPostSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = ProviderAdmin
        fields = ["first_name", "last_name", "email"]  # status excluded

    def create(self, validated_data):
        first_name = validated_data.pop("first_name")
        last_name = validated_data.pop("last_name")
        email = validated_data.pop("email")

        user = User.objects.create(
            username=email,
            first_name=first_name,
            last_name=last_name,
            email=email
        )


        return ProviderAdmin.objects.create(user=user)

    def update(self, instance, validated_data):
        first_name = validated_data.pop("first_name", None)
        last_name = validated_data.pop("last_name", None)
        email = validated_data.pop("email", None)

        # Update linked User
        user = instance.user
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        if email:
            user.email = email
            user.username = email
        user.save()


        return super().update(instance, validated_data)


class ProviderAdminGetSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source="user.first_name", read_only=True)
    last_name = serializers.CharField(source="user.last_name", read_only=True)
    email = serializers.EmailField(source="user.email", read_only=True)
    last_login = serializers.DateTimeField(source="user.last_login", read_only=True)
   

    class Meta:
        model = ProviderAdmin
        fields = ["id","first_name","last_name","email","status","last_login"]
