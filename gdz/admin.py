from django.contrib import admin
from .models import GdzClas, GdzSubject, GdzBook


@admin.register(GdzClas)
class GdzClasAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'update_time', 'uri')
    list_filter = ('slug', 'create_time')
    search_fields = ('slug', 'title')
    exclude = ['uri']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(GdzSubject)
class GdzSubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'update_time', 'gdz_clas', 'uri')
    list_filter = ('slug', 'create_time')
    search_fields = ('slug', 'title')
    raw_id_fields = ('gdz_clas',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(GdzBook)
class GdzBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'slug', 'update_time', 'gdz_clas', 'gdz_subject', 'uri')
    list_filter = ('gdz_clas', 'gdz_subject')
    search_fields = ('slug', 'title')
    raw_id_fields = ('gdz_clas', 'gdz_subject')
    prepopulated_fields = {'slug': ('title',)}