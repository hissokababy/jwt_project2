import time
import pika

from broker.rabbit import Rabbit
# from rabbit import Rabbit
time.sleep(10)

credentials = pika.PlainCredentials('rabbitmq', 'rabbitmq')
connection_params = pika.ConnectionParameters(host='rabbit', credentials=credentials)
rabbit = Rabbit(connection_params)

rabbit.create_exchange(exchange='video_hosting', exchange_type='direct')


@rabbit.message_handler(queue='user_statuses', auto_ack=True, 
                         exchange='video_hosting', routing_key='user_statuses')
def user_status_handler(ch, method, properties, body):
    print(f' [x] Received {body}')


@rabbit.message_handler(queue='registration', auto_ack=True, 
                         exchange='video_hosting', routing_key='registration')
def user_registration_handler(ch, method, properties, body):
    print(f' [x] Received {body}')
