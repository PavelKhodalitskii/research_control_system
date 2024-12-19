from django.contrib import admin
from .models import SystemUser

# Register your models here.

@admin.register(SystemUser)
class SystemUserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SystemUser._meta.fields]
