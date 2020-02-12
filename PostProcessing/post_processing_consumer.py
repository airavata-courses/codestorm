from confluent_kafka import Consumer, KafkaError
import pickle

c = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': '0',
    'auto.offset.reset': 'earliest'
})

c.subscribe(['ModelExecution'])

def pp_consumer():
    print("Entering consumer!@@")
    while True:
        msg = c.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            continue
        data = pickle.loads(msg.value())
        print("Model consumer : ", data)
        # print('Received message: {}'.format(msg.value().decode('utf-8')))
        c.close()
        print("Returning from pp_consumer!!!!!!!!!!!!")
        return(msg.value())
