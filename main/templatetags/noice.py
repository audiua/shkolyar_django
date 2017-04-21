from django import template

register = template.Library()

@register.inclusion_tag('main/noice.html', name='noice')
def noice():
    return {}