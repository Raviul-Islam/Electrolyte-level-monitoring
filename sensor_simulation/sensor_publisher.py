import paho.mqtt.client as mqtt
import time
import random

# MQTT client setup
mqtt_client = mqtt.Client()
mqtt_client.connect("broker.hivemq.com", 1883, 60)  # Replace with your MQTT broker details

while True:
    # Simulate electrolyte level (random number between 0 and 100)
    electrolyte_level = random.randint(0, 100)
    mqtt_client.publish("hospital/electrolyte", electrolyte_level)
    print(f"Published: {electrolyte_level}%")
    time.sleep(5)  # Publish data every 5 seconds
