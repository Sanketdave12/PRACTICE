from django.contrib import admin
from MAMARA.models import notice , Branch , Profile
from django.contrib.admin.options import ModelAdmin
# Register your models here.

class NoticeAdmin(ModelAdmin):
    list_display = ['name','date']
    search_fields = ['msg']
    list_filter = ['date']


admin.site.register(notice,NoticeAdmin) 
admin.site.register(Branch)
admin.site.register(Profile)