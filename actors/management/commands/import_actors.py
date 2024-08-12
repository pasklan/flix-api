import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from actors.models import Actor

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help='Nome do Arquivo CSV com atores')

    def handle(self, *args, **options):
        filename = options['filename']

        with open(filename, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row['name']
                birthday = datetime.strptime(row['birth_date'], '%Y-%m-%d').date()
                nationality = row['nationality']

                self.stdout.write(self.style.NOTICE(f'Ator: {name}'))

                Actor.objects.create(
                    name=name,
                    birthday=birthday,
                    nationality=nationality
                )

        self.stdout.write(self.style.SUCCESS('Arquivo importado com sucesso!'))