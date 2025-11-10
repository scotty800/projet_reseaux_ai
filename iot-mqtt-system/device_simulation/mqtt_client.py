import paho.mqtt.client as mqtt
import time

client = mqtt.Client()
client.connect("localhost", 1883)
client.loop_start()

def publish_temp(value):
    client.publish("iot/temp", value)