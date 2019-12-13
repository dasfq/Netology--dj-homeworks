from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv, urllib
from .settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    all_stations_list = []
    rows_per_page = 10
    with open(BUS_STATION_CSV) as file:
        reader = csv.DictReader(file)
        for row in reader:
            all_stations_list.append({"Name": row["Name"], "Street": row["Street"], "District": row["District"]})
        file.close()
    p = Paginator(all_stations_list, rows_per_page)
    page_number = 1 if request.GET.get('page') == None else int(request.GET.get('page'))
    if p.page(page_number).has_next():
        next_page_url = reverse('bus_stations') + '?' + urllib.parse.urlencode({'page': p.page(page_number).next_page_number()})
    else:
        next_page_url = None
    if p.page(page_number).has_previous():
        prev_page_url = reverse('bus_stations') + '?' + urllib.parse.urlencode(
        {'page': p.page(page_number).previous_page_number()})
    else:
        prev_page_url = None
    return render_to_response('index.html', context={
        'bus_stations': p.page(page_number),
        'current_page': page_number,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })

