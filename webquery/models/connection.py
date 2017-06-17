from django.contrib import admin
from django import forms
from django.db import models

from .engines import detect_db_engines


class Connection(models.Model):
    """Define the Connection model"""
    name = models.CharField(max_length=255, primary_key=True)
    description = models.CharField(max_length=255)
    engine = models.CharField(max_length=255,
                              choices=detect_db_engines())
    connection_string = models.TextField()
    server = models.CharField(max_length=255, blank=True)
    database = models.CharField(max_length=255, blank=True)
    username = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=255, blank=True)
    encoding = models.ForeignKey('Encoding')

    def __str__(self):
        """Return the Connection name"""
        return self.name


class ConnectionForm(forms.ModelForm):
    class Meta:
        widgets = {
            'password': forms.PasswordInput,
        }


class ConnectionAdmin(admin.ModelAdmin):
    """Define the visible fields"""
    form = ConnectionForm
    list_display = ['name',
                    'description',
                    'engine']
