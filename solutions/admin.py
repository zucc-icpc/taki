from django.contrib import admin
from solutions.models import Solution


class SolutionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner')


admin.site.register(Solution, SolutionAdmin)