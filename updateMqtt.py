import paho.mqtt.publish as publish
import json
import config

def updateMqtt(moisture, temperature, humidity, air_quality, light):
    payload = json.dumps({
        'moisture': moisture,
        'temperature': temperature,
        'humidity': humidity,
        'air_quality': air_quality,
        'light': light
    })
    publish.single(config.MQTT_TOPIC, payload, hostname=config.MQTT_HOST)

