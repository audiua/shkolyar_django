from django import template

register = template.Library()

@register.filter(name="section_name")
def section_name(value):
    return value.split('_')[1]