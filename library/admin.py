from django.contrib import admin
from .models import LibraryAuthor, LibraryBook
import datetime


@admin.register(LibraryBook)
class LibraryBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'library_author', 'title', 'slug', 'time_format', 'uri', )
    list_filter = ('library_author',)
    search_fields = ('slug', 'title')
    raw_id_fields = ('library_author', )
    exclude = ['vk_img', 'vk_public_time', 'length', 'nausea', 'description']
    fields = ('library_author', 'title', 'slug', 'uri', 'public', 'public_time')
    prepopulated_fields = {'slug': ('title',)}


    def time_format(self, obj):
        return datetime.datetime.fromtimestamp(float(obj.update_time))

@admin.register(LibraryAuthor)
class LibraryAuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'slug', 'uri')
    # list_filter = ('slug', 'create_time')
    search_fields = ('slug', 'author')
    prepopulated_fields = {'slug': ('author',)}