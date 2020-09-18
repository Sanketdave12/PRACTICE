from django.contrib import admin
from .models import SDDD
from django.contrib.admin.options import ModelAdmin

# Register your models here.
class SanketAdmin(ModelAdmin):
    list_display = ['name','date']
    search_fields = ['date']
    list_filter = ['date']



admin.site.register(SDDD,SanketAdmin)