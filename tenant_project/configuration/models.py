from django.db import models
from django.contrib.postgres.fields import JSONField
from timezone_field import TimeZoneField  


class Configuration(models.Model):
    time_zone = TimeZoneField(default="US/Eastern")
    email = models.EmailField(unique=True)
    email_verify=models.BooleanField(default=False)
    caller_id=models.CharField(max_length=150)
    caller_id_verify=models.BooleanField(default=False)

    #provider communication
    email=models.BooleanField(default=False)
    sms=models.BooleanField(default=False)
    notification=models.BooleanField(default=False)


    #patient communication
    email=models.BooleanField(default=False)
    sms=models.BooleanField(default=False)
    notification=models.BooleanField(default=False)

    smtp=models.BooleanField(default=False)
    alerts=models.BooleanField(default=False)


    def __str__(self):
        return f"Configuration ({self.email})"