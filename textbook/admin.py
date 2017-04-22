from django.contrib import admin
from .models import TextbookClas, TextbookSubject, TextbookBook


@admin.register(TextbookClas)
class TextbookClasAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'update_time', 'uri')
    list_filter = ('slug', 'create_time')
    search_fields = ('slug', 'title')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(TextbookSubject)
class TextbookSubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'update_time', 'textbook_clas', 'uri')
    list_filter = ('slug', 'create_time')
    search_fields = ('slug', 'title')
    raw_id_fields = ('textbook_clas',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(TextbookBook)
class TextbookBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'slug', 'update_time', 'textbook_clas', 'textbook_subject', 'uri')
    list_filter = ('textbook_clas', 'textbook_subject')
    search_fields = ('slug', 'title')
    raw_id_fields = ('textbook_clas', 'textbook_subject')
    prepopulated_fields = {'slug': ('author',)}