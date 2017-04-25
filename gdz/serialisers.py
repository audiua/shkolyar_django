from django.core.urlresolvers import reverse
from .models import GdzClas, GdzBook, GdzSubject
from rest_framework import serializers

class GdzClasSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="gdz_api:gdzclas-detail")
    class Meta:
        model = GdzClas
        fields = ('id', 'title', 'slug', 'create_time', 'update_time',
                  'description', 'is_promote', 'uri', 'url')

class GdzSubjectSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="gdz_api:gdzsubject-detail")
    gdz_clas = serializers.HyperlinkedIdentityField(view_name="gdz_api:gdzclas-detail")
    class Meta:
        model = GdzSubject
        fields = ('id', 'title', 'slug', 'create_time', 'update_time',
                  'description', 'is_promote', 'uri', 'url', 'gdz_clas')

class GdzBookSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="gdz_api:gdzbook-detail")
    gdz_clas = serializers.HyperlinkedIdentityField(view_name="gdz_api:gdzclas-detail")
    gdz_subject = serializers.HyperlinkedIdentityField(view_name="gdz_api:gdzsubject-detail")

    class Meta:
        model = GdzBook
        fields = ('id', 'author', 'slug', 'create_time', 'update_time',
                  'description', 'is_promote', 'uri', 'url', 'gdz_clas', 'gdz_subject')