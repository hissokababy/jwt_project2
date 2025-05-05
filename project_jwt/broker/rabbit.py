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
        

    def create_queue(self, queue: Any, passive: bool=False, durable: bool=False, 
                     exclusive: bool=False, auto_delete: bool=False, arguments: Any=None):
        
        result = self.channel().queue_declare(queue, passive, durable, 
                     exclusive, auto_delete, arguments)
        
        print(f'connection was set, queue "{queue}" created')
        
        queue_name = result.method.queue

        return queue_name
        

    def create_exchange(self, exchange: str, exchange_type: ExchangeType|str, passive: bool=False, durable: bool=False, 
                        auto_delete: bool=False, internal: bool=False, arguments=None):
        
        self.channel().exchange_declare(exchange, exchange_type, passive, durable, 
                        auto_delete, internal, arguments)
                

    def publish(self, queue: Any, exchange: str, routing_key: str, body: str, properties=None, 
                mandatory: bool=False, passive: bool=False, durable: bool=False, 
                     exclusive: bool=False, auto_delete: bool=False, arguments: Any=None):
        
        self.create_queue(queue=queue, passive=passive, durable=durable, exclusive=exclusive,
                          auto_delete=auto_delete, arguments=arguments)
        
        with self.channel() as channel:
            channel.basic_publish(exchange, routing_key, body, properties, mandatory)
            channel.close()
        print('Message was sent')
