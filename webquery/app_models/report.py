from django.contrib import admin
from django.db import models


class Report(models.Model):
    """Define the Report model"""
    name = models.CharField(max_length=255, primary_key=True)
    description = models.CharField(max_length=255)
    template = models.CharField(max_length=255)

    def __str__(self):
        """Return the Report name"""
        return self.name


class ReportAdmin(admin.ModelAdmin):
    """Define the visible fields"""
    list_display = ['name',
                    'description']

