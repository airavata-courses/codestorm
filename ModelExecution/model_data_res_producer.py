from confluent_kafka import Producer
import pickle
import json

p = Producer({'bootstrap.servers': 'localhost:9092'})


def md_producer(file):
    print(type(file))
    json_obj = pickle.dumps(file)
    p.produce('ModelExecution', key="imgur_link", value=json_obj)
    p.flush()
    print("Uploaded successfully in the kafka with topic ModelExecution !!!!!!!!!!!!!!!!!!!!!!!!!!")
    return "Uploaded successfully in the kafka with topic ModelExecution !!!!!!!!!!!!!!!!!!!!!!!!!!"


# Delievery Report
def delivery_report(err, msg):

    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))



