from django.contrib import admin

from .models import Folder, FolderAdmin
from .models import Encoding, EncodingAdmin
from .models import Report, ReportAdmin
from .models import Parameter, ParameterAdmin


# Registered models for admin
admin.site.register(Folder, FolderAdmin)
admin.site.register(Encoding, EncodingAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Parameter, ParameterAdmin)
