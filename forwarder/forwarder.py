import paho.mqtt.client as mqtt

MQTT_PORT=1883
MQTT_TOPIC="face_images"

# Open Issues:
# a. Identify local container by name
LOCAL_MQTT_HOST="mqtt_broker"

REMOTE_MQTT_HOST="mqtt_broker"

def on_connect_local(client, userdata, flags, rc):
    print("connected to local broker with rc: " + str(rc))
    localclient.subscribe(MQTT_TOPIC) 

def on_connect_remote(client, userdata, flags, rc):
    print("connected to remote broker with rc: " + str(rc))

def on_publish(client, userdata, mid):
    print("message {} successfully published!".format(mid))

def on_message(client, userdata, msg):
    try:
        print("message received!")
        data = msg.payload
        remoteclient.publish("random", payload=data, qos=0, retain=False)
    except:
        print("Unexpected error:", sys.exc_info()[0])

localclient = mqtt.Client()
localclient.on_connect = on_connect_local
localclient.connect(LOCAL_MQTT_HOST, MQTT_PORT, 60)
localclient.on_message = on_message

remoteclient = mqtt.Client()
remoteclient.on_connect = on_connect_remote
remoteclient.connect(REMOTE_MQTT_HOST, MQTT_PORT, 60)
remoteclient.on_publish = on_publish

localclient.loop_forever()
