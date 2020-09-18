from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
# Register your models here.
from HEHE2_APP import models


class NoticeAdmin(ModelAdmin):
    list_display = ["name",'date']
    search_fields = ['name','msg']
    list_filter = ['date']



admin.site.register(models.notice,NoticeAdmin)