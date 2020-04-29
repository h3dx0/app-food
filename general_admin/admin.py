from django.contrib import admin

# Register your models here.
from general_admin.models import User, UserType

admin.site.site_header = "Portal de administracion"
admin.site.site_title = "Portal de administracion"
admin.site.index_title = "Bienvenidos al portal de administración"

admin.site.register(User)
admin.site.register(UserType)