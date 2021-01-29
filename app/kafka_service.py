from datetime import datetime

from kafka import KafkaConsumer
from kafka import KafkaProducer
import json

from torch import FloatTensor
from torchmodels.evaluator import evaluator

consumer_topic = 'python_test'
consumer = KafkaConsumer(
    consumer_topic,
    value_deserializer=lambda v: json.loads(v),
    bootstrap_servers='118.138.243.91:9092'
)

producer_topic = 'model_test'
producer = KafkaProducer(
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    bootstrap_servers='118.138.243.91:9092'
)

print("consuming...")
for msg in consumer:
    # Parse input data
    value = msg.value
    inp = FloatTensor([value["magnitude"], value["angle"]])
    
    # Run evaluator on msg
    prediction = evaluator(inp)
    producer.send(producer_topic, {'prediction': prediction, 'time': str(datetime.now())})
