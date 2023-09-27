import json
from kafka import KafkaConsumer

if __name__ == '__main__':
    # Kafka Consumer
    consumer = KafkaConsumer(
        'messages-new',
        #'ime',
        bootstrap_servers='localhost:29092',
        #bootstrap_servers='localhost:9992',
        auto_offset_reset='earliest',
        fetch_max_bytes = 500000
    )
    for message in consumer:
        print(message.key, json.loads(message.value))