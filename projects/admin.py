from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'link', 'order', 'is_active', 'open_in_new_tab')
    list_editable = ('order', 'is_active')
    search_fields = ('title', 'category', 'link')
    prepopulated_fields = {'slug': ('title',)}