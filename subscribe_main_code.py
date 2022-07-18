#데이터 전송 확인해보려고 수정중(태인)

import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)


def on_disconnect(client, userdata, flags, rc=0):
    print(str(rc))


def on_subscribe(client, userdata, mid, granted_qos):
    print("subscribed: " + str(mid) + " " + str(granted_qos))


def on_message(client, userdata, msg):
    print(str(msg.payload.decode("utf-8")))

#data = []

# 새로운 클라이언트 생성
client = mqtt.Client()


# 콜백 함수 설정 on_connect(브로커에 접속), on_disconnect(브로커에 접속중료), on_subscribe(topic 구독),
# on_message(발행된 메세지가 들어왔을 때)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_subscribe = on_subscribe
client.on_message = on_message

# address : localhost, port: 1883 에 연결
client.connect('localhost', 20518)

# common topic 으로 메세지 발행
csv = client.subscribe('common', 1)   # csv파일을 읽어와서 변수에 저장
#data.append(csv)   # 빈 리스트에 읽어온 데이터 추가

#print(data)
client.loop_forever()