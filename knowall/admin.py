from django.contrib import admin
from .models import Knowall, KnowallCategory, KnowallGrab
import datetime


@admin.register(Knowall)
class KnowallAdmin(admin.ModelAdmin):
    list_display = ('id', 'knowall_category', 'title', 'slug', 'time_format', 'uri', )
    list_filter = ('knowall_category',)
    search_fields = ('slug', 'title')
    raw_id_fields = ('knowall_category', )
    exclude = ['vk_img', 'vk_public_time', 'length', 'nausea', 'description']
    fields = ('knowall_category', 'title', 'slug', 'uri', 'text', 'public', 'public_time')
    prepopulated_fields = {'slug': ('title',)}


    def time_format(self, obj):
        return datetime.datetime.fromtimestamp(float(obj.update_time))

@admin.register(KnowallCategory)
class KnowallCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'uri')
    # list_filter = ('slug', 'create_time')
    search_fields = ('slug', 'title')


@admin.register(KnowallGrab)
class KnowallGrabAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')
    search_fields = ('slug', 'title')