#!/usr/bin/env python
import pika
import time
import requests
import argparse 
#from LED import LED_random 
import json

parser = argparse.ArgumentParser()
parser.add_argument('-ip', dest='client_pi',help='ip address')
args = parser.parse_args()
client_ip = args.client_pi

credentials = pika.PlainCredentials('team25','team25')
connection = pika.BlockingConnection(pika.ConnectionParameters(host="172.29.38.28",credentials=credentials))
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
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)
    # issue request to change user status in AuthDB
    r = requests.put('http://172.29.47.154:5000/change_status', json={'Tag': tag, 'Status': 1})  # set user status to 1 == logged in

    if(r.ok):
        print(r.content)
    else:
        print(r.status_code)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='RFID_Queue')

channel.start_consuming()
