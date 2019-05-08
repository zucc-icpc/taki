from django.contrib import admin
from user.models import User, Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'updated_at', 'type', 'name', 'sid', 'level')


admin.site.register(Profile, ProfileAdmin)