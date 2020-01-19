# w251-hw

To test this setup on my local system (TX2), I disabled mosquitto running on the host.

```
root@vijay-desktop:~# sudo service --status-all
 [ - ]  alsa-utils
...
[ + ]  mosquitto
```
```
sudo systemctl stop mosquitto
```

Then I created a new bridge network that will connect all the host side containers. An advantage of the custom bridge network is that container names can be resolved to their IP addresses.

```
docker network create --driver bridge mqtt
6859c4eebe6954c77a60b99964f347340439fe6ec446712bb4adf1764b9fd68d
docker network ls
NETWORK ID          NAME                DRIVER              SCOPE
8e3e9c406caa        bridge              bridge              local
d3165b4f0dbe        host                host                local
6859c4eebe69        mqtt                bridge              local
fafb44cb59dc        none                null                local
```

Then I ran the mqttb image that I had built that started the mosquitto broker in a container running Alpine:

```
docker run --rm --name mqtt_broker --net mqtt -p 1883:1883 -it mqttb
1579394675: mosquitto version 1.6.8 starting
1579394675: Using default config.
1579394675: Opening ipv4 listen socket on port 1883.
1579394675: Opening ipv6 listen socket on port 1883.

vijay@vijay-desktop:~$ sudo docker ps
CONTAINER ID        IMAGE               COMMAND                 CREATED              STATUS              PORTS               NAMES
a344d84a59f1        mqttb               "/usr/sbin/mosquitto"   About a minute ago   Up About a minute   1883/tcp            mqtt_broker
```

The next step is to build the MQTT forwarder, which will subscribe to the local broker and publish to the VM broker. The instructions are to have this running in a container built on Alpine Linux. In addition to the packages needed for the broker, we need python3 and paho-mqtt in this container.

While running this container, I put this container also in the bridge network I created earlier. This container is running a python script that usis paho-mqtt to setup two MQTT connections - one to the local broker, and another to the remote broker running in the cloud VM. Once the connection to the local broker is established, the local client subscribes to the topic "face_images" on which is expecting messages to be received.

Here's how this container was run:

```
docker run --rm --privileged -e DISPLAY -v /tmp:/tmp --net mqtt -it face_capture
connected to local broker with rc: 0
Corrupt JPEG data: 5 extraneous bytes before marker 0xd7

(img:1): dbind-WARNING **: 03:22:24.234: Couldn't connect to accessibility bus: Failed to connect to socket /tmp/dbus-kRsyNM3o4b: Connection refused
Gtk-Message: 03:22:24.412: Failed to load module "canberra-gtk-module"
Gtk-Message: 03:22:24.422: Failed to load module "canberra-gtk-module"
message 1 successfully published!
Corrupt JPEG data: 1 extraneous bytes before marker 0xd7
message 2 successfully published!
```

