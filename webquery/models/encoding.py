from django.contrib import admin
from django.db import models


class Encoding(models.Model):
    """Define the Encoding model"""
    name = models.CharField(max_length=255, primary_key=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        """Return the Encoding name"""
        return self.name


class EncodingAdmin(admin.ModelAdmin):
    """Define the visible fields"""
    list_display = ['name',
                    'description']

