from django.core.management.base import BaseCommand, CommandParser
from myapp.models import Client
from typing import Any

class Command(BaseCommand):
    help = 'Update a user by their ID'

    def add_arguments(self, parser: CommandParser):
        parser.add_argument('pk', type=int, help='User\'s ID')
        parser.add_argument('field', type=str, help='Field to update')
        parser.add_argument('value', help='New value')

    def handle(self, *args: Any, **kwargs: Any):
        pk = kwargs.get('pk')
        field = kwargs.get('field')
        value = kwargs.get('value')
        user_to_update = Client.objects.filter(pk=pk)
        if field == 'first_name':
            user_to_update.update(first_name=value)
            self.stdout.write(f'User {pk} updated successfully!')
        elif field == 'last_name':
            user_to_update.update(last_name=value)
            self.stdout.write(f'User {pk} updated successfully!')
        elif field == 'email':
            user_to_update.update(email=value)
            self.stdout.write(f'User {pk} updated successfully!')
        elif field == 'phone':
            user_to_update.update(phone=value)
            self.stdout.write(f'User {pk} updated successfully!')
        elif field == 'address':
            user_to_update.update(address=value)
            self.stdout.write(f'User {pk} updated successfully!')
        else: 
            self.stdout.write(f'Field name can\'t be recognised or it is unchangeable')