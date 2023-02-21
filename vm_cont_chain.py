import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
	print("Connected to server (i.e., broker) with result code "+str(rc))
	client.subscribe("tmajam/ping")
	
	client.message_callback_add("tmajam/ping", on_message_from_ping)
	
def on_message(client, userdata, message):
	print("Default message callback - topic: " + message.topic + " message: " + str(message.payload, "uft-8"))
	
#Custom callback message for ping topic
def on_message_from_ping(client, userdata, message):
	next = int(message.payload.decode()) + 1
	print("Custom callback - Count " + f"{next}")
	client.publish("tmajam/pong", f"{next}")
	time.sleep(1)
	
if __name__ == '__main__':
	client = mqtt.Client()
	client.on_message = on_message_from_ping
	client.on_connect = on_connect
	
	client.connect(host="192.168.3.192", port=1883, keepalive=60)
	
	client.loop_forever()
