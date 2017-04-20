import time
from django import template
from textbook import models
register = template.Library()


@register.inclusion_tag('textbook/textbook_menu.html', name='textbook_menu', takes_context=True)
def textbook_menu(context):
    items = models.TextbookSubject.objects.filter(subject_textbooks__public=1,
                                             subject_textbooks__lte=time.time())

    menu_items = {}
    for item in items:
        if item.textbook_clas not in menu_items:
            menu_items[item.textbook_clas] = []
        menu_items[item.textbook_clas].append(item.textbook_clas)

    return {'items': menu_items}

