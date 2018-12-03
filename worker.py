#!/usr/bin/env python
import pika
import time
import requests
import argparse 
#from LED import LED_random 
import json
from LED import LED_random

parser = argparse.ArgumentParser()
parser.add_argument('-cip', dest='client_pi',help='client ip address')
parser.add_argument('-dip', dest='database_pi',help='database ip address')
parser.add_argument('-s', dest='seat',help='seat number')
args = parser.parse_args()
client_ip = args.client_pi
database_ip = args.database_pi
seat = args.seat
led = LED_random("red")

credentials = pika.PlainCredentials('team25','team25')
connection = pika.BlockingConnection(pika.ConnectionParameters(host=client_ip,credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='RFID_Queue', durable=True)

print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    payload = json.loads(body)
    color = payload["Color"]
    tag = payload["Tag"]
    print(tag)
    print(color)
    #LED_random.flashLED(color)
    time.sleep(body.count(b'.'))
    
    # issue request to change user status in AuthDB
    r = requests.put('http://'+database_ip+':5000/change_status', json={'Tag': tag, 'Status': 1})  # set user status to 1 == logged in

    if(r.ok):
        print(r.content)
        info = r.json
        led.flashLED();
    else:
        print(r.status_code)

    # Update the global variables in the Flask App
    r = requests.put('http://'+client_ip+':5000/update_info', json={'Color': color, 'Seat': seat, 'Name': info['Name']})

    if(r.ok):
        print(r.content)
    else:
        print(r.status_code)

    ch.basic_ack(delivery_tag = method.delivery_tag)
    print(" [x] Done")

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='RFID_Queue')

channel.start_consuming()
