from django.contrib import admin

from .models import UUIDRequest
# Register your models here.


@admin.register(UUIDRequest)
class UUIDRequestAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'created', 'id']