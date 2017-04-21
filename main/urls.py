from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^about/$', views.about, name='about'),
    url(r'^contacts/$', views.contact, name='contact'),
    url(r'^rightholder/$', views.rightholder, name='rightholder'),
    url(r'', views.index, name='index')
]