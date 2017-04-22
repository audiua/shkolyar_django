import time
from django import template
from textbook import models
register = template.Library()

LAST_ITEMS_COUNT = 8

@register.inclusion_tag('textbook/textbook_last_items.html', name='textbook_last_items', takes_context=True)
def textbook_last_items(context):
    items = models.TextbookBook.published.order_by('-public_time')[:LAST_ITEMS_COUNT]

    return {'items': items}
