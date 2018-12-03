#!/usr/bin/env python
import pika
import time
import requests
import argparse 

client_ip = "0.0.0.0"
parser = argparse.ArgumentParser()
parser.add_argument('-ip', dest='client_ip',required = True, help='Setting the client IP')
credentials = pika.PlainCredentials('team25','team25')
connection = pika.BlockingConnection(pika.ConnectionParameters(host=client_ip,credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='RFID_Queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)
    # issue request to change user status in AuthDB
    r = requests.put('', data={'Status': '1'})  # set user status to 1 == logged in
    print(r.text)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='RFID_Queue')

channel.start_consuming()
