from django.contrib import admin

from .models import Folder, FolderAdmin

# Registered models for admin
admin.site.register(Folder, FolderAdmin)
