from django.contrib import admin

from .models import Folder, FolderAdmin
from .models import Encoding, EncodingAdmin


# Registered models for admin
admin.site.register(Folder, FolderAdmin)
admin.site.register(Encoding, EncodingAdmin)
