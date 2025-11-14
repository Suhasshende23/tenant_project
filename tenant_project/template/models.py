from django.db import models

class TemplateTypeChoices(models.TextChoices):
    SMS="SMS"
    EMAIL="Email"
    NOTE="Note"

class Template(models.Model):
    name = models.CharField(max_length=150)
    template_type=models.CharField(max_length=150,choices=TemplateTypeChoices)
    subject=models.CharField(max_length=300,blank=True,null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)