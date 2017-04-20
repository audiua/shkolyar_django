import time
from django import template
from writing import models
register = template.Library()


@register.inclusion_tag('writing/writing_menu.html', name='writing_menu', takes_context=True)
def textbook_menu(context):
    items = models.WritingSubject.objects.filter(subject_writings__public=1,
                                             subject_writings__lte=time.time())


    menu_items = {}
    for item in items:
        if item.writing_clas not in menu_items:
            menu_items[item.writing_clas] = []
        if item not in menu_items[item.writing_clas]:
            menu_items[item.writing_clas].append(item)

    return {'items': menu_items}

