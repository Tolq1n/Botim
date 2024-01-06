from django.contrib import admin
from .models import User
# Register your models here.


# admin.site.register(User)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'genereted_key', 'full_name', 'sending_time', 'joined_at', 'username', 'mute']
    list_display_links = ['id', 'genereted_key', 'full_name', 'sending_time', 'joined_at', 'username', 'mute']