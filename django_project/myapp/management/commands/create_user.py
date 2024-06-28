from django.core.management.base import BaseCommand, CommandParser
from myapp.models import Client
from typing import Any

class Command(BaseCommand):
    help = 'Create a user'

    def add_arguments(self, parser: CommandParser):
        parser.add_argument('first_name', type=str, help='User\'s first name')
        parser.add_argument('last_name', type=str, help='User\'s last_name')
        parser.add_argument('email', type=str, help='User\'s email')
        parser.add_argument('phone', type=int, help='User\'s phone')
        parser.add_argument('address', type=str, help='User\'s address')

    def handle(self, *args: Any, **kwargs: Any):
        first_name = kwargs['first_name']
        last_name = kwargs['last_name']
        email = kwargs['email']
        phone = kwargs['phone']
        address = kwargs['address']
        user = Client(first_name=first_name, last_name=last_name, email=email, phone=phone, address=address)
        user.save()
