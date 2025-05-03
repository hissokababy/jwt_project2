import pika

from broker.rabbit import Rabbit

def rabbit_connect(host: str, username: str, password: str):
    connection_params = pika.ConnectionParameters(host=host, credentials=pika.PlainCredentials(username, password))
    rabbit = Rabbit(connection_params)
    return rabbit
