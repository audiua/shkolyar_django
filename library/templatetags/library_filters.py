from django import template

register = template.Library()

@register.filter('fix_library_img')
def fix_library_img(value):
    return value.replace('src="/library/description/', 'src="/static/library/description/')
