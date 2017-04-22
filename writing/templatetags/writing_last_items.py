import time
from django import template
from writing import models
register = template.Library()

LAST_ITEMS_COUNT = 6

@register.inclusion_tag('writing/writing_last_items.html', name='writing_last_items', takes_context=True)
def writing_last_items(context):
    items = models.Writing.published.order_by('-public_time')[:LAST_ITEMS_COUNT]

    return {'items': items}
