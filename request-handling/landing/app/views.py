import math
from collections import Counter
from django.http import HttpResponse

from django.shortcuts import render_to_response

counter_show = Counter()
counter_click = Counter()


def index(request):
    root = request.GET.get('from-landing')
    counter_click[root] += 1
    print(counter_show)
    return render_to_response('index.html')


def landing(request):
    page_type = request.GET.get('ab-test-arg')
    counter_show[page_type] += 1
    if page_type == 'original':
        return render_to_response('landing.html')
    elif page_type == "test":
        return render_to_response('landing_alternate.html')


def stats(request):
    try:
       test_conversion = counter_click['test'] / counter_show['test']
    except ArithmeticError:
        test_conversion = 0
    try:
        original_conversion = counter_click['original'] / counter_show['original']
    except: original_conversion = 0

    return render_to_response('stats.html', context={
        'test_conversion': test_conversion,
        'original_conversion': original_conversion,
    })
