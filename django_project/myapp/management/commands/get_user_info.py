from django.core.management.base import BaseCommand, CommandParser
from myapp.models import Client
from typing import Any

class Command(BaseCommand):
    help = 'Get user info by their ID'

    def add_arguments(self, parser: CommandParser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args: Any, **kwargs: Any):
        pk = kwargs['pk']
        user = Client.objects.filter(pk=pk).first()
        self.stdout.write(f'{user}')