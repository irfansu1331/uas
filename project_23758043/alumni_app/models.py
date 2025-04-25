from django.conf import settings
from django.db import models

class Alumni(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    nama = models.CharField(max_length=255)
    email = models.EmailField()
    graduation_year = models.IntegerField()
    major = models.CharField(max_length=255)
    job_position = models.CharField(max_length=255)
    company = models.CharField(max_length=255)

    def __str__(self):
        return self.nama
