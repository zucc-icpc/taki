from django.contrib import admin
from honors.models import Honor


class HonorAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'time')


admin.site.register(Honor, HonorAdmin)