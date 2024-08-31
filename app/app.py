from flask import Flask, render_template, jsonify
import paho.mqtt.client as mqtt

app = Flask(__name__)

# Global variable to hold the electrolyte level
level = 100  # Default level

# MQTT callback function
def on_message(client, userdata, message):
    global level
    level = int(message.payload.decode("utf-8"))

# MQTT client setup
mqtt_client = mqtt.Client()
mqtt_client.on_message = on_message
mqtt_client.connect("broker.hivemq.com", 1883, 60)  # Replace with your MQTT broker details
mqtt_client.subscribe("hospital/electrolyte")
mqtt_client.loop_start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    return jsonify({'level': level})

if __name__ == '__main__':
    app.run(debug=True)
