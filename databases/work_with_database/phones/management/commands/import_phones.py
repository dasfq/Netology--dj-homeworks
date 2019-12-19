import csv, os

from django.core.management.base import BaseCommand
from phones.models import Phone
import os

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:
            phone_reader = csv.reader(csvfile, delimiter=';')
            next(phone_reader)

            for line in phone_reader:
                item = Phone.objects.create(
                             name = line[1],
                             slug = line[1].replace(' ', '-'),
                             image = line[2],
                             price = line[3],
                             release_date = line[4],
                             lte_exists = line[5])
