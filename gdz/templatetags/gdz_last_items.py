import time
from django import template
from gdz import models
register = template.Library()

LAST_ITEMS_COUNT = 8

@register.inclusion_tag('gdz/gdz_last_items.html', name='gdz_last_items', takes_context=True)
def gdz_last_items(context):
    items = models.GdzBook.published.order_by('-public_time')[:LAST_ITEMS_COUNT]

    return {'items': items}
