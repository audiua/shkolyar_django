from django.contrib import admin
from .models import WritingClas, WritingSubject, Writing


@admin.register(WritingClas)
class WritingClasAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'uri')
    list_filter = ('slug', 'create_time')
    search_fields = ('slug', 'title')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(WritingSubject)
class WritingSubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'writing_clas', 'uri')
    list_filter = ('slug', 'writing_clas' )
    search_fields = ('slug', 'title',)
    raw_id_fields = ('writing_clas',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Writing)
class WritingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'update_time', 'clas', 'subject', 'uri', 'public')
    list_filter = ('clas', 'subject')
    search_fields = ('slug', 'title')
    raw_id_fields = ('clas', 'subject')
    prepopulated_fields = {'slug': ('title',)}