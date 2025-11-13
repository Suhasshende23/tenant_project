from django.db import models


class Flag(models.Model):
    color=models.CharField(max_length=30)
    name=models.CharField(max_length=150)
    description=models.TextField()
    patient_count=models.IntegerField()
    created_by=models.CharField(max_length=100)

    