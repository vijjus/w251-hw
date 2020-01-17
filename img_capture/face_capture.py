import numpy as np
import cv2 as cv
import paho.mqtt.client as mqtt

print(cv.__version__)

# Open Issues:
# a. Identify local container by name
# b. Encode messages for transmission
# c. Ensure only faces are captured
LOCAL_MQTT_HOST="localhost"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="face_images"

def on_connect_local(client, userdata, flags, rc):
    print("connected to local broker with rc: " + str(rc))

def on_publish(client, userdata, mid):
    print("message {} successfully published!".format(mid))

mqttclient = mqtt.Client()
mqttclient.on_connect = on_connect_local
mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
mqttclient.on_publish = on_publish

model_file="/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml"
# 1 should correspond to /dev/video1 , your USB camera. The 0 is reserved for the TX2 onboard camera
cap = cv.VideoCapture(1)
face_cascade = cv.CascadeClassifier(model_file)

mqttclient.loop_start()

count=0
while True:
    ret, frame = cap.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        cv.imshow('img',frame)
        count += 1
        mqttclient.publish(LOCAL_MQTT_TOPIC, count)
    cv.waitKey(0)

cv.destroyAllWindows()
