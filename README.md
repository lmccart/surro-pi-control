## Install
* Install ngrok:
  ```
  wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip (https://dashboard.ngrok.com/get-started/setup)
  unzip ngrok-stable-linux-VERSION.zip
  rm ngrok-stable-linux-VERSION.zip
  chmod 755 ngrok
  sudo mv ngrok /usr/bin/
  ```
* Install motor hat drivers https://www.waveshare.com/wiki/Motor_Driver_HAT
* Install git: `sudo apt install git`
* Install flask: `sudo pip install flask`



## Running
Manual:
```
cd Surrogate
export FLASK_APP=.
export FLASK_ENV=development
flask run
ngrok http 5000
```
With script (starts flask and ngrok to custom surrogate_tunnel endpoint:
```
./start-flask.sh
./start-ngrok.sh
```


## Pi Utils
* scan for PI IPs: `arp -na | grep -i b8:27:eb`
* setup wifi: `sudo nano /etc/wpa_supplicant/wpa_supplicant.conf`

## References
* flask: https://flask.palletsprojects.com/en/2.0.x/tutorial/factory/
* motor hat: https://www.waveshare.com/wiki/Motor_Driver_HAT
* ngrok: https://dashboard.ngrok.com/get-started/setup
* https://www.techcoil.com/blog/how-to-host-your-python-3-flask-mvp-with-supervisor-on-ubuntu-server-16-04/
* 
