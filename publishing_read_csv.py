import paho.mqtt.client as mqtt
import json
import csv
import time
import glob
import os

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)


def on_disconnect(client, userdata, flags, rc=0):
    print(str(rc))


def on_publish(client, userdata, mid):
    print("In on_pub callback mid= ", mid)


# 새로운 클라이언트 생성
client = mqtt.Client()
# 콜백 함수 설정 on_connect(브로커에 접속), on_disconnect(브로커에 접속중료), on_publish(메세지 발행)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish
# address : localhost, port: 1883 에 연결
client.connect('203.250.148.119', 20518)

# client.loop_start()

client.loop_start()

# common topic 으로 메세지 발행
client.loop_start()



# 디렉토리에 있는 모든 파일을 읽은후 값을 전송 시켜줌.
# MQTT= (메세지 큐잉 프로토콜임)

file_directory=os.listdir("../project/picam/accel/")
myfile='filename.csv'
for filename in file_directory:
    
    if filename == myfile:
        continue

    #file='../project/picam/accel/20220512_1047.csv'
    with open('../project/picam/accel/'+filename, 'r') as read_obj:
        data = read_obj.read()
    client.publish('common', data)

    # time.sleep(5)


        
    client.loop_stop()

# 연결 종료
client.disconnect()

#for문으로 돌리기