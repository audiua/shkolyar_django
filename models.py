# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Ankor(models.Model):
    ankor = models.CharField(max_length=255)
    to_uri = models.CharField(max_length=255)
    entity_class = models.CharField(max_length=255)
    entity_id = models.IntegerField()
    before_ankor = models.CharField(max_length=255, blank=True, null=True)
    after_ankor = models.CharField(max_length=255, blank=True, null=True)
    entity_type = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ankor'





class BannerDump(models.Model):
    name = models.CharField(max_length=255)
    code = models.TextField(blank=True, null=True)
    create_time = models.IntegerField()
    update_time = models.IntegerField()
    title = models.CharField(max_length=255)
    on = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'banner_dump'


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    img = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    task_path = models.CharField(max_length=255)
    lang = models.CharField(max_length=255)
    properties = models.CharField(max_length=255, blank=True, null=True)
    pagination = models.CharField(max_length=255, blank=True, null=True)
    ping_google = models.IntegerField()
    public = models.IntegerField()
    create_time = models.IntegerField()
    update_time = models.IntegerField()
    public_time = models.IntegerField()
    subject = models.ForeignKey('Subject', models.DO_NOTHING, blank=True, null=True)
    class_field = models.ForeignKey('Clas', models.DO_NOTHING, db_column='class_id', blank=True, null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'book'


class Clas(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    create_time = models.IntegerField()
    update_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clas'


class Description(models.Model):
    owner = models.CharField(max_length=255)
    action = models.CharField(max_length=255)
    clas_id = models.IntegerField()
    subject_id = models.IntegerField()
    description = models.TextField()
    create_time = models.IntegerField()
    update_time = models.IntegerField()
    page_mode = models.CharField(max_length=255, blank=True, null=True)
    block_id = models.IntegerField()
    category_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'description'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DpaAnswer(models.Model):
    slug = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    clas = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    create_at = models.IntegerField()
    update_at = models.IntegerField()
    public_at = models.IntegerField()
    public = models.IntegerField()
    author = models.CharField(max_length=255)
    uri = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'dpa_answer'


class DpaTask(models.Model):
    slug = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    clas = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    create_at = models.IntegerField()
    update_at = models.IntegerField()
    public_at = models.IntegerField()
    public = models.IntegerField()
    uri = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'dpa_task'


class FosUser(models.Model):
    username = models.CharField(max_length=180)
    username_canonical = models.CharField(unique=True, max_length=180)
    email = models.CharField(max_length=180)
    email_canonical = models.CharField(unique=True, max_length=180)
    enabled = models.IntegerField()
    salt = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255)
    last_login = models.DateTimeField(blank=True, null=True)
    confirmation_token = models.CharField(unique=True, max_length=180, blank=True, null=True)
    password_requested_at = models.DateTimeField(blank=True, null=True)
    roles = models.TextField()

    class Meta:
        managed = False
        db_table = 'fos_user'











class Keyword(models.Model):
    keyword = models.CharField(max_length=255)
    create_time = models.IntegerField()
    update_time = models.IntegerField()
    url = models.CharField(max_length=255)
    check_keyword = models.IntegerField()
    google_view = models.IntegerField()
    yandex_view = models.IntegerField()
    sape_url_id = models.BigIntegerField()
    sape_get_links_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'keyword'


class KeywordPosition(models.Model):
    google_position = models.IntegerField()
    yandex_position = models.IntegerField()
    create_time = models.IntegerField()
    keyword_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'keyword_position'







class Link(models.Model):
    from_url = models.CharField(max_length=255)
    on_url = models.CharField(max_length=255)
    create_time = models.IntegerField()
    update_time = models.IntegerField()
    check_link = models.IntegerField()
    ankor = models.CharField(max_length=255)
    links_on_donor = models.IntegerField()
    check_time = models.IntegerField()
    sape_link_id = models.BigIntegerField()
    link_source = models.CharField(max_length=255, blank=True, null=True)
    vk_public_time = models.IntegerField()
    jj_public_time = models.IntegerField()
    tw_public_time = models.IntegerField()
    keyword = models.ForeignKey(Keyword, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'link'


class Mistake(models.Model):
    page_url = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField()
    resolved = models.IntegerField()
    owner = models.CharField(max_length=255, blank=True, null=True)
    owner_id = models.IntegerField(blank=True, null=True)
    session_id = models.CharField(max_length=255)
    filename = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mistake'


class PageWeigth(models.Model):
    page_url = models.CharField(max_length=255)
    link_url = models.CharField(max_length=255)
    link_ankor = models.CharField(max_length=255)
    link_nofollow = models.IntegerField()
    link_context = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'page_weigth'





class Position(models.Model):
    create_time = models.IntegerField()
    keyword_id = models.IntegerField()
    g_position = models.IntegerField()
    y_position = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'position'


class Refferal(models.Model):
    url = models.CharField(max_length=255)
    block = models.TextField()

    class Meta:
        managed = False
        db_table = 'refferal'


class RelevantPage(models.Model):
    ankor = models.ForeignKey(Ankor, models.DO_NOTHING, blank=True, null=True)
    from_uri = models.CharField(max_length=255)
    created_at = models.IntegerField()
    entity_class = models.CharField(max_length=255)
    entity_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'relevant_page'


class Setting(models.Model):
    field = models.CharField(primary_key=True, max_length=255)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'setting'


class SocialPosting(models.Model):
    owner = models.CharField(max_length=255)
    owner_id = models.IntegerField()
    create_time = models.IntegerField()
    social = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'social_posting'


class Subject(models.Model):
    title = models.CharField(unique=True, max_length=255)
    slug = models.CharField(unique=True, max_length=255)
    create_time = models.IntegerField()
    update_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'subject'


class Task(models.Model):
    slug = models.CharField(max_length=255)
    section_slug = models.CharField(max_length=255, blank=True, null=True)
    section_desc = models.CharField(max_length=255, blank=True, null=True)
    paragraph_slug = models.IntegerField(blank=True, null=True)
    paragraph_desc = models.CharField(max_length=255, blank=True, null=True)
    page_slug = models.IntegerField(blank=True, null=True)
    page_desc = models.CharField(max_length=255, blank=True, null=True)
    book_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'task'





class Tizer(models.Model):
    tema = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    public = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tizer'


class TranslatePage(models.Model):
    html = models.TextField()
    url = models.TextField()
    title = models.TextField(blank=True, null=True)
    h1 = models.TextField(blank=True, null=True)
    created_at = models.IntegerField()
    updated_at = models.IntegerField()
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'translate_page'


class User(models.Model):
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'user'





class VkTimePosting(models.Model):
    gdz_last_public_time = models.IntegerField(blank=True, null=True)
    textbook_last_public_time = models.IntegerField(blank=True, null=True)
    writing_last_public_time = models.IntegerField(blank=True, null=True)
    library_last_public_time = models.IntegerField(blank=True, null=True)
    author_last_public_time = models.IntegerField(blank=True, null=True)
    knowall_last_public_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vk_time_posting'





class Zno(models.Model):
    title = models.CharField(max_length=70, blank=True, null=True)
    h1 = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    subject_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'zno'


class ZnoAnswer(models.Model):
    slug = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=4)
    author = models.CharField(max_length=255)
    subject = models.CharField(max_length=25)
    description = models.TextField(blank=True, null=True)
    create_at = models.IntegerField()
    update_at = models.IntegerField()
    public_at = models.IntegerField()
    public = models.IntegerField()
    uri = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'zno_answer'


class ZnoTask(models.Model):
    slug = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=4)
    author = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    create_at = models.IntegerField()
    update_at = models.IntegerField()
    public_at = models.IntegerField()
    public = models.IntegerField()
    uri = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'zno_task'


class ZnoVidpovidi(models.Model):
    title = models.CharField(max_length=70, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    h1 = models.CharField(max_length=255, blank=True, null=True)
    subject_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'zno_vidpovidi'
