from django import template

register = template.Library()

@register.filter(name='inflation_filter')
def color_filter(value, row):
    index = row.index(value)
    try:
        value = float(value)
        if index + 1 == len(row):
            return 'grey'
        elif index != 0 and index != 13:
            if value < 0:
                return 'green'
            elif 1 < value < 2:
                return '#FA8072'
            elif 2 <= value < 5:
                return '#B22222'
            elif value >= 5:
                return '#8B0000'
    except:
        value = value