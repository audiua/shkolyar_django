import time
from django import template
from knowall import models
register = template.Library()

LAST_ITEMS_COUNT = 6

@register.inclusion_tag('knowall/knowall_last_items.html', name='knowall_last_items', takes_context=True)
def knowall_last_items(context):
    items = models.Knowall.published.order_by('-public_time')[:LAST_ITEMS_COUNT]

    return {'items': items}
