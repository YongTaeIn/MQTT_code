#pika모듈을 이용한 통신

#!/usr/bin/env python
import pika, sys, os

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',20518,'/',pika.PlainCredentials('guest', 'guest')))
    channel = connection.channel()

    #queue를 선언(declare)
    channel.queue_declare(queue='hello')

    #Receiving 받을 함수 handler 정의
    #callback 함수는 pika 라이브러리에 의해 호출
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body.decode())

    #Queue가 'hello'의 consuming 설정
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    #consuming start
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)