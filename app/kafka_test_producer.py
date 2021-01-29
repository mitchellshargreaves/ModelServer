import time
from datetime import datetime

from kafka import KafkaProducer
import json

producer = KafkaProducer(
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    bootstrap_servers='118.138.243.91:9092'
    )

topic = 'python_test'

print("publishing...")
while True:
    producer.send(topic, {'magnitude': 0, 'angle': 90, 'time': str(datetime.now())})
    time.sleep(0.02) # Sleep for 1/50 seconds to mimic pmu
