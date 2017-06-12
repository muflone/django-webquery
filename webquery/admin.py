from django.contrib import admin

from .models.folder import Folder, FolderAdmin
from .models.encoding import Encoding, EncodingAdmin
from .models.report import Report, ReportAdmin
from .models.parameter import Parameter, ParameterAdmin
from .models.connection import Connection, ConnectionAdmin


# Registered models for admin
admin.site.register(Folder, FolderAdmin)
admin.site.register(Encoding, EncodingAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Parameter, ParameterAdmin)
admin.site.register(Connection, ConnectionAdmin)
