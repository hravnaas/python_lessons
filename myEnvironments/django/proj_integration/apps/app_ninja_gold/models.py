from __future__ import unicode_literals

from django.db import models
from ..secrets.models import Secret

# Bogus class/model to test using a class (Secret) from another app.
class Activity(models.Model):
    entry = models.CharField(max_length=255)
    secret = models.ForeignKey(Secret)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
