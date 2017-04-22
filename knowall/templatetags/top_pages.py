import time
from django import template
from main import models as main_models
from knowall import models as knowall_models
register = template.Library()

LAST_ITEMS_COUNT = 5

@register.inclusion_tag('knowall/top_pages.html', name='top_pages', takes_context=True)
def top_pages(context):
    print(context['request'].path)
    items = main_models.ViewCount.objects.filter(uri__contains="/knowall") \
                .exclude(uri=context['request'].path)\
                .order_by('-counter')[:LAST_ITEMS_COUNT]

    print(items)

    articles = knowall_models.Knowall.published\
        .filter(uri__in=[item.uri for item in items])


    return {'articles': articles}
