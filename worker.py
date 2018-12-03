#!/usr/bin/env python
import pika
import time
import requests

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
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


channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='RFID_Queue')

channel.start_consuming()
