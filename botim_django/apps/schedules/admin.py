from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import WeekDay, Schedule, DayKind, TimeConfig


admin.site.register(TimeConfig)

@admin.register(Schedule)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'weekday', 'daykind', 'subject', 'lesson_type', 'teacher', 'room']
    list_display_links = ['id', 'user', 'weekday', 'daykind', 'subject', 'lesson_type', 'teacher', 'room']


class WeekDayAdmin(TranslatableAdmin):
    list_display = ('name', 'id')
    fieldsets = (
        (None, {
             'fields': ('name',),
        }),
    )
admin.site.register(WeekDay, WeekDayAdmin)


class DayKindAdmin(TranslatableAdmin):
    list_display = ('name', 'id')
    fieldsets = (
        (None, {
             'fields': ('name',),
        }),
    )
admin.site.register(DayKind, DayKindAdmin)

# admin.site.register(DayKind)