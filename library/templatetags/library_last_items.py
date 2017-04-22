import time
from django import template
from library import models
register = template.Library()

LAST_ITEMS_COUNT = 6

@register.inclusion_tag('library/library_last_items.html', name='library_last_items', takes_context=True)
def library_last_items(context):
    items = models.LibraryBook.published.order_by('-public_time')[:LAST_ITEMS_COUNT]

    return {'items': items}
