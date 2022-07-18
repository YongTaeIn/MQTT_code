#pika모듈을 이용한 통신

#!/usr/bin/env python
import pika
 
#RabbitMQ 서버에 연결
#connection과 channel를 생성

connection = pika.BlockingConnection(
    pika.ConnectionParameters('203.250.148.119',20518,'/',pika.PlainCredentials('sohyun', 'aisl1234!')))
channel = connection.channel()


#queue_declare: channel를 통해 queue 선언(declare)
channel.queue_declare(queue='hello')
 
#channel의 publish(sending)
#routing_key: Queue 이름
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print(" [x] Sent 'Hello World!'")
 
#connection 연결 종료
connection.close()