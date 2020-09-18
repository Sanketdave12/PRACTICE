from django.contrib import admin
from .models import sd
from django.contrib.admin.options import ModelAdmin

# Register your models here.
class sdAdmin(ModelAdmin):
    list_display = ['name','msg']
    search_fields = ['email','msg']
    list_filter = ['date']


admin.site.register(sd,sdAdmin)