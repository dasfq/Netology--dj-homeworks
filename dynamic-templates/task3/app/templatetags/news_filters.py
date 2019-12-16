from django import template
from datetime import datetime
from dateutil import parser
import time
from math import *
from itertools import chain


register = template.Library()


@register.filter
def format_date(value):
    now = parser.parse(time.ctime(time.time()))
    post_time = parser.parse(time.ctime(value))
    time_delta = now - post_time
    if (time_delta.seconds / 60) < 10:
        return "Только что"
    elif (time_delta.seconds / 60 / 60) < 24:
        return f'{ceil(time_delta.seconds / 60 / 60)} часов назад'
    elif (time_delta.seconds / 60 / 60) >= 24:
        return post_time


@register.filter(name='score_filter')
def score_filter(value, default):
    if value == False:
        return default
    else:
        if value < -5:
            return "Всё плохо"
        elif -5 <= value < 5:
            return "Нейтрально"
        elif value >= 5:
            return "Хорошо"

@register.filter
def format_num_comments(value):
    if value == 0:
        return "Оставьте комментарий"
    elif 0 < value < 50:
        return value
    elif value >= 50:
        return "50+"
    return value


@register.filter
def format_selftext(value, count):
    text = value.split()
    length = len(text)
    start_index = count
    finish_index = length - count
    replace_with = ['...']
    if length < count * 2 + 2:
        return value
    else:
        return " ".join(list(chain(text[:start_index], replace_with, text[finish_index:])))