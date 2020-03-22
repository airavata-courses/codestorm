from confluent_kafka import Consumer, KafkaError
import pickle

c = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': '0',
    'auto.offset.reset': 'earliest'
})

c.subscribe(['DataRetrieval'])

def md_consumer():
    print("Started Consuming")
    msg = None
    while msg is None:
        msg = c.poll(1.0)
    if msg is None:
        print("No message") 
        # continue
        #return "No message"
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        # continue
    if msg.value()==None:
        return None
    data = pickle.loads(msg.value())
    print("Model consumer : !!!!!!!!!!!!!!!!!!!!!!!!", data)
    print("Returning from md_consumer!!!!")
    return data
    c.close()
   
