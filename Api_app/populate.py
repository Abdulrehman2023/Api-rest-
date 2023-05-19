import random
import string
from django.core.management.base import BaseCommand
from Api_app.models import APi_default

class Command(BaseCommand):
    name = 'populate_script
    help = 'Populates the APi_default model with 10 records.'

    def handle(self, *args, **options):
        for _ in range(10):
            firstname = ''.join(random.choices(string.ascii_uppercase, k=5))
            lastname = ''.join(random.choices(string.ascii_uppercase, k=5))
            email = ''.join(random.choices(string.ascii_lowercase, k=5)) + '@example.com'
            APi_default.objects.create(Firstname=firstname, Lastname=lastname, Email=email)