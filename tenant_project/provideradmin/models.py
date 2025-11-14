from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
class ProviderAdmin(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="provider_admin")
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.user.email
