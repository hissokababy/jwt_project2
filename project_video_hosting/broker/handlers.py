from broker.rabbit import Rabbit
# from rabbit import Rabbit
import pika

connection_params = pika.ConnectionParameters('rabbit', credentials=pika.PlainCredentials('rabbitmq', 'rabbitmq'))
rabbit = Rabbit(connection_params)

@rabbit.consume_messages(queue='registration', auto_ack=True)
def message_handler(ch, method, properties, body):
    print(f' [x] Received {body}') 

# @rabbit.consume_messages(queue='hello', auto_ack=True)
# def message_handler(ch, method, properties, body):
#     print(f' [x] Received {body}') 


rabbit.run()





