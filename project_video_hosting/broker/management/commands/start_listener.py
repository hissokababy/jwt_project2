from django.core.management.base import BaseCommand
import pika

from broker import handlers

from broker.rabbit import Rabbit

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        credentials = pika.PlainCredentials('rabbitmq', 'rabbitmq')
        connection_params = pika.ConnectionParameters(host='rabbit', credentials=credentials)

        rabbit = Rabbit(connection_params=connection_params)

        rabbit.run()


