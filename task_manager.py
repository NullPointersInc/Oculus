"""Task mamanger script to unify all different features in Oculus."""
import paho.mqtt.client as mqtt
import time
import os
import argparse
import sys


def on_connect(client, userdata, flags, rc):
    """on_connect is used to check connection to broker."""
    if rc == 0:

        print("Connected to broker: " + str(broker_address))
        global Connected  # Use global variable
        Connected = True  # Signal connection

    else:
        print("Connection failed to " + str(broker_address))


def on_message(client, userdata, message):
    """Perform operations when message is received."""
    op = str(message.payload.decode("utf-8"))
    print(op)
    if op == 'object':
        os.system("sh run_detection.sh -o")
    elif op == 'currency':
        os.system(
            "sshpass -p 'bella12345' \
             scp pi@192.168.0.9:~/image/image.jpg ./classify_note/")
        os.system("sh run_detection.sh -n")
    elif op == 'face':
        os.system(
            "sshpass -p 'bella12345' scp pi@192.168.0.9:~/image/image.jpg .")
        os.system("mv image.jpg classify_person/")
        os.system("sh run_detection.sh -p")
    elif op == 'prediction':
        os.system(
            "sshpass -p 'bella12345' \
             scp pi@192.168.0.9:~/image/image.jpg ./im2txt/data")
        os.system("sh run_detection.sh -l")
    elif op == 'ocr':
        os.system(
            "sshpass -p 'bella12345' \
             scp pi@192.168.0.9:~/image/image.jpg ./OCR")
        os.system("python3 OCR/ocr.py --image image.jpg")
    else:
        print("Pass")


def get_args_values(args=None):
    """Method to handle command line arguments."""
    parser = argparse.ArgumentParser(description="Arguments supported..")
    parser.add_argument('-H', '--host',
                        help='Broker IP',
                        default='localhost')
    parser.add_argument('-p', '--port',
                        help='port of the Broker',
                        default='1883')
    parser.add_argument('-u', '--user',
                        help='user name',
                        default='astr1x')
    parser.add_argument('-P', '--password',
                        help="password",
                        default='astr1x2096')

    info = parser.parse_args(args)
    return (info.host,
            info.port,
            info.user,
            info.password)


"""
Get Broker address, port, username and password.
The default value has already been provided.
"""
if __name__ == '__main__':
    broker_address, port, user, password = get_args_values(sys.argv[1:])
    port = int(port)


Connected = False  # global variable for the state of the connection

client = mqtt.Client("Oculus-Server")  # create new instance
client.username_pw_set(user, password=password)  # set username and password
client.on_connect = on_connect  # attach function to callback
client.on_message = on_message  # attach function to callback


print("Connecting to broker")
client.connect(broker_address, port=port)  # connect to broker

client.loop_start()


while Connected is not True:  # Wait for connection
    time.sleep(0.1)

print("Subscribing to topic Oculus")
client.subscribe("Oculus")

try:
    while True:
        time.sleep(0.1)
except (KeyboardInterrupt, SystemExit):
    print()
    print("Exiting..")
    client.disconnect()
    client.loop_stop()
