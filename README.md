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
