from django.db import models
from tenant_project.icd.models import ICD

# Optional: Program choices for future use
class ProgramChoices(models.TextChoices):
    CCM = "CCM", "CCM"
    PCM = "PCM", "PCM"
    RPM = "RPM", "RPM"
    BHM = "BHM", "BHM"

class Condition(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=200, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    icd = models.ForeignKey(ICD, on_delete=models.CASCADE, related_name="conditions")

    def __str__(self):
        return f"{self.name} ({self.icd.code})"
