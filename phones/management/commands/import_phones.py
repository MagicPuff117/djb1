

import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as f:
            phone_reader = csv.reader(f, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)
            for line in phone_reader:
                phone = Phone(
                    id=int(line[0]), name=line[1], image=line[2],
                    price=line[3], release_date=line[4],
                    lte_exists=line[5]
                )
                print(phone)
                phone.save()