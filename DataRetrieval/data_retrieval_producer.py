from confluent_kafka import Producer
import pickle
import json

p = Producer({'bootstrap.servers': 'localhost:9092'})


def dr_producer(file):
    print(type(file))
    json_obj = pickle.dumps(file)
    p.produce('DataRetrieval', key="filename", value=json_obj)
    p.flush()


# Delievery Report
def delivery_report(err, msg):

    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))
