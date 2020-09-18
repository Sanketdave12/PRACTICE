from django.contrib import admin
from HEHE.models import Notice , Branch , Profile
from django.contrib.admin import ModelAdmin
# Register your models here.

class NoticeAdmin(ModelAdmin):
    list_display = ['name','date']
    search_fields = ['msg']
    list_filter = ['date']


admin.site.register(Notice,NoticeAdmin) 
admin.site.register(Branch)
admin.site.register(Profile)