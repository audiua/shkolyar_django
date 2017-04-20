import time
from collections import OrderedDict
from PIL import Image
from natsort import natsorted
from os import path, listdir
from django import template
from django.conf import settings
from gdz import models
register = template.Library()


@register.inclusion_tag('gdz/gdz_tasks.html', name='gdz_tasks', takes_context=True)
def gdz_menu(context):
    book = context['gdz_book']
    clas = context['gdz_clas']
    subject = context['gdz_subject']
    dir = path.join(settings.BASE_DIR, 'images', 'gdz', clas.slug, subject.slug, book.slug, 'task')
    items = [{'section': item, 'dir': dir, 'childs': (listdir(path.join(dir, item)))} for item in listdir(dir)]

    for item in items:
        # print(item)
        images = []
        for child in item['childs']:
            sub_dir = path.join(item['dir'], item['section'], child) #item=unit, child=lesson
            if path.isdir(sub_dir):
                sub_tasks = {
                    'section': child, 'dir': sub_dir
                }

                sub_images = []
                for sub_item in listdir(sub_dir):
                    sub_image_dir = path.join(item['dir'], item['section'], child, sub_item)
                    sub_img_path = path.join('gdz', clas.slug, subject.slug, book.slug, 'task', item['section'], child, sub_item)
                    sub_image_info = image_info(dir=sub_image_dir, child=sub_item, img_path=sub_img_path)

                    sub_images.append(sub_image_info)

                sub_tasks['childs'] = sub_images
                images.append(sub_tasks)
            else:
                image_dir = path.join(item['dir'], item['section'], child)
                img_path = path.join('gdz', clas.slug, subject.slug, book.slug, 'task', item['section'], child)
                img_info = image_info(dir=image_dir, child=child, img_path=img_path)
                images.append(img_info)


        images = natsorted(images)
        item['childs'] = images

    # items = natsorted(items)
    # print(item)
    return {'data': items, 'book': book}


def image_info(dir=None, child=None, img_path=None):
    im = Image.open(dir)
    width, heigth = im.size
    number = child.split('.')[0]
    return {'name': child, 'width': width,
                   'heigth': heigth, 'task_number': number,
                   'img_path': img_path}