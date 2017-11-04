import paho.mqtt.client as mqtt
import time
import os

def msg(client, userdata, message):
    op = str(message.payload.decode("utf-8"))
    if op == 'object':
        os.system("sh run_detection.sh")
    elif op == 'money':
        time.sleep(3)
        os.system("sshpass -p 'qwerty12345' scp pi@192.168.0.5:~/oculus/image.jpg .")
        os.system("mv image.jpg classify_note/")
        os.system("sh classify_note.sh")
    elif op == 'faces':
        time.sleep(3)
        os.system("sshpass -p 'qwerty12345' scp pi@192.168.0.5:~/oculus/image.jpg .")
        os.system("mv image.jpg classify_person/")
        os.system("sh classify_person.sh")

broker_addr = "192.168.0.5"
client = mqtt.Client("tm")
client.on_message = msg

print ("Connecting to broker")
client.connect(broker_addr)
print ("Subscribing to topic oculus")
while True:
    client.loop_start()
    client.subscribe("oculus")
    time.sleep(1)
    client.loop_stop()
