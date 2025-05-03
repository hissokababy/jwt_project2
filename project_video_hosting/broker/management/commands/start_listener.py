from django.core.management.base import BaseCommand

from broker import handlers


class Command(BaseCommand):
    
    def handle(self, *args, **options):
        print("fsdfsdf")
        handlers.rabbit.run()

