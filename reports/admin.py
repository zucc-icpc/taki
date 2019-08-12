from django.contrib import admin
from reports.models import Report


class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner')


admin.site.register(Report, ReportAdmin)