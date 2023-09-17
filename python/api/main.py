from utils import random

from fastapi import FastAPI

from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092']
)

app = FastAPI()

@app.get("/api/v1/")
async def root():
    return {"message": "pingpong!"}

@app.patch("/api/v1/messages/push")
async def push_message():
    message: str = f"Hello, {random.random_string(16)}!".encode('ascii')
    try:
        producer.send("greats", message)
    except KafkaError:
        return {"message": "Failed to push message into apache kafka."}

    return {"message": message}

