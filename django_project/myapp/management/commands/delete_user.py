from django.core.management.base import BaseCommand, CommandParser
from myapp.models import Client
from typing import Any

class Command(BaseCommand):
    help = 'Delete a user by their ID'

    def add_arguments(self, parser: CommandParser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args: Any, **kwargs: Any):
        pk = kwargs['pk']
        user = Client.objects.filter(pk=id).first()
        if user is not None:
            user.delete()
            self.stdout.write('User deleted successfully!')
        else: 
            self.stdout.write('User with this ID does not exist!')
