from django.contrib import admin
from django.db import models


class Parameter(models.Model):
    """Define the Parameter model"""
    name = models.CharField(max_length=255, primary_key=True)
    description = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        """Return the Parameter name"""
        return self.name


class ParameterAdmin(admin.ModelAdmin):
    """Define the visible fields"""
    list_display = ['name',
                    'description']

