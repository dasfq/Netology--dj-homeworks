from django import template

register = template.Library()

@register.filter(name='pricetag')
def pricetag(value):
    return str(value) + 'р.'

@register.filter(name='presence_filter')
def presence(value):
    if not value:
        return '-'
    else:
        return "+"