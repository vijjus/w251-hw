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

Then I ran the mqttb image that I had built that started the mosquitto broker in a container running Alpine:

```
root@vijay-desktop:~# docker run --name mqtt_broker mqttb
1579394675: mosquitto version 1.6.8 starting
1579394675: Using default config.
1579394675: Opening ipv4 listen socket on port 1883.
1579394675: Opening ipv6 listen socket on port 1883.

vijay@vijay-desktop:~$ sudo docker ps
CONTAINER ID        IMAGE               COMMAND                 CREATED              STATUS              PORTS               NAMES
a344d84a59f1        mqttb               "/usr/sbin/mosquitto"   About a minute ago   Up About a minute   1883/tcp            mqtt_broker
```
