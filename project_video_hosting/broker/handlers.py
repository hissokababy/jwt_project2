import pika

from broker.rabbit import Rabbit

credentials = pika.PlainCredentials(username='rabbitmq', password='rabbitmq')
rabbit = Rabbit(pika.ConnectionParameters(host='rabbit', credentials=credentials, connection_attempts=5))

rabbit.create_exchange(exchange='test', exchange_type='direct')
test_queue = rabbit.create_queue(queue='', exchange='test', routing_key='test')


@rabbit.message_handler(queue=test_queue, auto_ack=True)
def user_status_handler(ch, method, properties, body):
    print(f'status handler: [x] Received {body}')





