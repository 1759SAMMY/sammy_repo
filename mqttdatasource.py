from paho.mqtt import client as mqtt
import json, time, random

broker = "EC2_PUBLIC_IP"
port = 1883
topic = "iot/sensors/room1"

client = mqtt.Client("simulator-01")
client.connect(broker, port)

while True:
    msg = {
        "deviceId": "sensor-01",
        "temperature": round(random.uniform(20, 30), 2),
        "humidity": round(random.uniform(40, 60), 2),
        "timestamp": int(time.time())
    }
    client.publish(topic, json.dumps(msg))
    print("Published:", msg)
    time.sleep(2)
