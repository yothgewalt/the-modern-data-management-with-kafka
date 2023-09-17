from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'stocks',
    group_id='stock-trackings',
    bootstrap_servers=['localhost:9092']
)

for message in consumer:    
    print(message.value)
