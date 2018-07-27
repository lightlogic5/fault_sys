from django.contrib import admin
from .models import ErrSysType, ErrSys


@admin.register(ErrSysType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')
    admin.AdminSite.site_header = 'aaaaaa'


@admin.register(ErrSys)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'err_type', 'author', 'readed_num', 'created_time', 'last_updated_time')

