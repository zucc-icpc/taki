from django.contrib import admin
from templates.models import Template


class TemplateAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner')


admin.site.register(Template, TemplateAdmin)