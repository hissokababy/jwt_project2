from django.core.management.base import BaseCommand
import time

from broker import handlers


class Command(BaseCommand):
    
    def handle(self, *args, **options):
        time.sleep(10)
        handlers.rabbit.run()


