import pika
from typing import Any
from pika.exceptions import AMQPConnectionError
from pika.exchange_type import ExchangeType
from pika.adapters.blocking_connection import BlockingChannel


class Rabbit:
    def __init__(self, connection_params: pika.ConnectionParameters):
        self.connection_params = connection_params
        self.message_handlers = []

    def channel(self) -> BlockingChannel:
        connection = pika.BlockingConnection(
            self.connection_params)
        channel = connection.channel()
        return channel


    def create_queue(self, queue: Any, passive: bool=False, durable: bool=False, 
                     exclusive: bool=False, auto_delete: bool=False, arguments: Any=None, 
                     exchange: Any=None, routing_key: Any=None, bind_args: Any=None):
        
        res = self.channel().queue_declare(queue, passive, durable, 
                     exclusive, auto_delete, arguments)
        queue_name = res.method.queue
        
        if exchange and routing_key:
            self.channel().queue_bind(queue=queue_name, exchange=exchange, routing_key=routing_key, arguments=bind_args)
        print(f'connection was set, queue {queue_name} created')
        return queue_name


    def create_exchange(self, exchange: str, exchange_type: ExchangeType|str, passive: bool=False, durable: bool=False, 
                        auto_delete: bool=False, internal: bool=False, arguments=None):
        self.channel().exchange_declare(exchange, exchange_type, passive, durable, 
                        auto_delete, internal, arguments)


    def message_handler(self, queue: str, auto_ack: bool=False, exclusive: bool=False, consumer_tag:Any=None, arguments:Any=None):
        def decorator(func):
            
            handler = {
                'queue': queue,
                'on_message_callback': func,
                'auto_ack': auto_ack,
                'exclusive': exclusive,
                'consumer_tag': consumer_tag,
                'arguments': arguments
            }

            self.message_handlers.append(handler)
            return func
        return decorator


    def run(self):
        with self.channel() as channel:
            for message_handler in self.message_handlers:
                channel.basic_consume(**message_handler)

            channel.start_consuming()

