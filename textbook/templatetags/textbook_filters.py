from django import template
import hashlib
from django.conf import settings
import PIL
import glob
import os


register = template.Library()

@register.filter(name="str_add")
def str_add(value, arg, *args):
    value = str(value)
    value += str(arg)
    for a in args:
        value += str(a)
    return value

@register.filter(name='md5')
def md5_string(value):
    return hashlib.md5(value.encode(encoding='UTF-8')).hexdigest()


@register.filter(name="first_img")
def get_first_image(value, arg):
    image_path = os.path.join(settings.BASE_DIR, 'images', value, 'article', str(arg))
    image = glob.glob("{}/*.*".format(image_path))[:1]
    image_name = image[0].split('/')[-1]
    return image_name

@register.filter('unix_date')
def unit_to_datetime(value):
    import datetime
    return datetime.datetime.fromtimestamp(int(value))

@register.filter('fix_img')
def fix_img(value):
    return value.replace('src="/knowall/article/', 'src="/static/knowall/article/')
