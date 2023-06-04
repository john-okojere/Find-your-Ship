from django.contrib import admin
from .models import  User
from import_export.admin import ImportExportMixin



class UserAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('username','first_name','last_name','phone','email','gender','role','is_staff','is_active','date_joined','update_fields',)
    list_filter = ('username','first_name','last_name','phone','email','gender','role','is_staff','is_active','date_joined','update_fields',)
    search_fields = ('username','first_name','last_name','phone','email','gender','role','is_staff','is_active','date_joined','update_fields',)
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)
admin.site.register(User, UserAdmin)
