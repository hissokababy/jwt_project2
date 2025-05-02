from typing import Any
import pika
from pika.exchange_type import ExchangeType


class Rabbit:
    def __init__(self, connection_params: pika.ConnectionParameters):

        self.connection = pika.BlockingConnection(
            connection_params)
        self.channel = self.connection.channel()


    def create_queue(self, queue: Any, passive: bool=False, durable: bool=False, 
                     exclusive: bool=False, auto_delete: bool=False, arguments: Any=None):
        
        result = self.channel.queue_declare(queue, passive, durable, 
                     exclusive, auto_delete, arguments)
        
        print(f'connection was set, queue "{queue}" created')
        
        queue_name = result.method.queue

        return queue_name
    
    def create_queue_bind(self, exchange: str, queue: str, routing_key):
        self.channel.queue_bind(exchange=exchange, queue=queue, routing_key=routing_key)
        print(f'{routing_key} was binded to {queue}')
        

    def create_exchange(self, exchange: str, exchange_type: ExchangeType|str, passive: bool=False, durable: bool=False, 
                        auto_delete: bool=False, internal: bool=False, arguments=None):
        
        self.channel.exchange_declare(exchange, exchange_type, passive, durable, 
                        auto_delete, internal, arguments)
                

    def publish(self, exchange: str, routing_key: str, body: str, properties=None, 
                mandatory: bool=False):
        
        self.channel.basic_publish(exchange, routing_key, body, properties, mandatory)
        print('message was sent')


    def consume_messages(self, queue: str, auto_ack: bool = False):
        self.channel.queue_declare(queue=queue)

        def decorator(func):
            self.channel.basic_consume(queue=queue, on_message_callback=func, auto_ack=auto_ack)
            print(f'Consuming messages from queue {queue}')

        return decorator
    
    def run(self):
        print('ready to consume messages...')
        self.channel.start_consuming()
