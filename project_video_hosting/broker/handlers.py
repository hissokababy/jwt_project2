import pika

from broker.rabbit import Rabbit
from video_hosting.validators import ValidateMessage
from video_hosting.services.user import VideoHostingService

credentials = pika.PlainCredentials(username='rabbitmq', password='rabbitmq')
rabbit = Rabbit(pika.ConnectionParameters(host='rabbit', credentials=credentials, connection_attempts=5))



rabbit.create_exchange(exchange='video_hosting_exchange', exchange_type='direct')
user_activity_queue = rabbit.create_queue(queue='', exchange='video_hosting_exchange', routing_key='user_activity')
user_register_queue = rabbit.create_queue(queue='', exchange='video_hosting_exchange', routing_key='user_register')


service = VideoHostingService()


@rabbit.message_handler(queue=user_activity_queue, auto_ack=True)
def user_activity_handler(ch, method, properties, body):
    message = ValidateMessage.validate_activity(body)

    service.change_user_activity(message.id, message.active)


@rabbit.message_handler(queue=user_register_queue, auto_ack=True)
def user_register_handler(ch, method, properties, body):
    message = ValidateMessage.validate_user_id(body)
    service.register_user(message.id)


