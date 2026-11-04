from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'kind', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('kind', 'is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)
    actions = ['mark_as_read']

    @admin.action(description='علامت‌گذاری به‌عنوان خوانده‌شده')
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)