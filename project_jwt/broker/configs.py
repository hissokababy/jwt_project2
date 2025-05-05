import pika

from broker.rabbit import Rabbit

connection_params = pika.ConnectionParameters(host='rabbit', credentials=pika.PlainCredentials('rabbitmq', 'rabbitmq'))
rabbit = Rabbit(connection_params)


