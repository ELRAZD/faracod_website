from django.contrib import admin
from .models import SiteSettings, IntroMessage, HeroSection, AboutSection, ContentBlock


class SingletonAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not self.model.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(SiteSettings)
class SiteSettingsAdmin(SingletonAdmin):
    pass


@admin.register(IntroMessage)
class IntroMessageAdmin(SingletonAdmin):
    pass


@admin.register(HeroSection)
class HeroSectionAdmin(SingletonAdmin):
    pass


@admin.register(AboutSection)
class AboutSectionAdmin(SingletonAdmin):
    pass


@admin.register(ContentBlock)
class ContentBlockAdmin(SingletonAdmin):
    pass