from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

websites = ['google.com', 'facebook.com', 'amazon.com', 'netflix.com']

while True:
    event = {
        'user_id': random.randint(1, 1000),
        'url': random.choice(websites),
        'timestamp': time.time()
    }
    producer.send('clickstream', value=event)
    print(f'Produced: {event}')
    time.sleep(1)