from django.contrib import admin
from .models import Feature


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'group', 'order', 'icon')
    list_filter = ('group',)
    list_editable = ('order',)
    search_fields = ('title',)