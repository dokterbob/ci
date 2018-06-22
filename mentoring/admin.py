from django.contrib import admin

from mentoring.models import SessionType, Session


@admin.register(SessionType)
class SessionTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_filter = ['session_type', 'progress']
    date_hierarchy = 'date'
    search_fields = ['student__name']
