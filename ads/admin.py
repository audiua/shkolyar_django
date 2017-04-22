from django.contrib import admin
from .models import Banner, BannerCode, Place, PlaceBanner

class BannerCodeInline(admin.TabularInline):
    model = BannerCode

class BannerInline(admin.TabularInline):
    model = Banner

@admin.register(Banner)
class AdminBanner(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_active')
    inlines = (BannerCodeInline,)


@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'type', 'entity', 'is_active')
    # filter_horizontal = ('banner',)
