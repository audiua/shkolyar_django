import time
from django import template
from knowall import models
register = template.Library()


@register.inclusion_tag('knowall/knowall_menu.html', name='knowall_menu', takes_context=True)
def knowall_menu(context):
    items = models.KnowallCategory.objects\
        .filter(articles__public=1, articles__public_time__lte=time.time())\
        .distinct()
    return {'items': items}

