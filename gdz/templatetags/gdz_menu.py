import time
from django import template
from gdz import models
register = template.Library()


@register.inclusion_tag('gdz/gdz_menu.html', name='gdz_menu', takes_context=True)
def gdz_menu(context):
    items = models.GdzSubject.objects.filter(gdz_subject_books__public=1,
                                             gdz_subject_books__lte=time.time())

    menu_items = {}
    for item in items:
        if item.gdz_clas not in menu_items:
            menu_items[item.gdz_clas] = []
        menu_items[item.gdz_clas].append(item.gdz_clas)

    return {'items': menu_items}

