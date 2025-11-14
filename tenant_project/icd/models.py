from django.db import models

class ICD(models.Model):
    title = models.CharField(max_length=300)
    code = models.CharField(max_length=150)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True) 
    condition = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.code} - {self.title}"
