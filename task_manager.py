"""Task mamanger script to unify all different features in Oculus."""
import paho.mqtt.client as mqtt
import time
import os
import argparse
import sys

status = False

# def checkMethod(flag):
#     """Method to check if object_detection is running or not."""
#     if(flag is True):
#         os.system("kill $!")
#         flag = False
#     return flag


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
    global status
    op = str(message.payload.decode("utf-8"))
    print(op)
    if op == 'object':
        if(status is True):
            os.system("pgrep -f 'python3 oculus.py' | xargs kill")
        status = True
        os.system("cd object_detection && python3 oculus.py &")
    elif op == 'currency':
        if(status is True):
            status = False
            os.system("pgrep -f 'python3 oculus.py' | xargs kill")
        os.system(
            "sshpass -p 'bella12345' \
             scp pi@192.168.43.59:~/image/image.jpg ./classify_note/")
        os.system("cd classify_person && python3 classify.py image.jpg")
    elif op == 'face':
        if(status is True):
            status = False
            os.system("pgrep -f 'python3 oculus.py' | xargs kill")
        os.system(
            "sshpass -p 'bella12345' \
            scp pi@192.168.43.59:~/image/image.jpg ./classify_person/")
        os.system("cd classify_note && python3 classify.py image.jpg")
    elif op == 'prediction':
        if(status is True):
            status = False
            os.system("pgrep -f 'python3 oculus.py' | xargs kill")
        os.system(
            "sshpass -p 'bella12345' \
             scp pi@192.168.43.59:~/image/image.jpg ./im2txt/data")
        os.system("sh image_labelling.sh")
    elif op == 'ocr':
        if(status is True):
            status = False
            os.system("pgrep -f 'python3 oculus.py' | xargs kill")
        os.system(
            "sshpass -p 'bella12345' \
             scp pi@192.168.43.59:~/image/image.jpg ./OCR")
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
