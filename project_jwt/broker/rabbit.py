from typing import Any
import pika
from pika.exchange_type import ExchangeType


class Rabbit:
    def __init__(self, connection_params: pika.ConnectionParameters):
        self.connection_params = connection_params
        self.message_handlers = []

    def channel(self):
        connection = pika.BlockingConnection(
            self.connection_params)
        channel = connection.channel()
        return channel
        

    def publish(self, exchange: str, routing_key: str, body: str, properties=None, 
                mandatory: bool=False):
        
        with self.channel() as channel:
            channel.basic_publish(exchange, routing_key, body, properties, mandatory)
            channel.close()
        print('Message was sent')
