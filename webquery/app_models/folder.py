from django.contrib import admin
from django.db import models


class Folder(models.Model):
    """Define the Folder model"""
    name = models.CharField(max_length=255, primary_key=True)
    description = models.CharField(max_length=255)
    visible = models.BooleanField(default=True)

    def __str__(self):
        """Return the Folder name"""
        return self.name


class FolderAdmin(admin.ModelAdmin):
    """Define the visible fields"""
    list_display = ['name',
                    'description',
                    'visible']
