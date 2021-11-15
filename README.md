## Install
* Install ngrok:
  ```
  wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm64.zip
  unzip ngrok-stable-linux-VERSION.zip
  rm ngrok-stable-linux-VERSION.zip
  chmod 755 ngrok
  sudo mv ngrok /usr/bin/
  ```
* [Setup ngrok](https://dashboard.ngrok.com/get-started/setup)
* Install motor hat drivers https://www.waveshare.com/wiki/Motor_Driver_HAT
* Install flask: `sudo pip install flask`
* Upgrade flask to 2.0: `pip install --upgrade Flask`
* Install flask dependencies: 
  * `pip install -U flask-cors`
* Install git: `sudo apt install git`
* [Generate ssh key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
* Clone repo: `git clone git@github.com:lmccart/womb-walk-pi.git`

## Running
Manual:
```
cd womb-walk-pi
python server.py
ngrok start womb_walk_tunnel
```
Howver, systemctl should run these

## ngrok
* Start tunnel from command line: `ngrok http --region=us --hostname=womb-walk.ngrok.io 80`
* https://dashboard.ngrok.com/endpoints/domains

## References
* flask: https://flask.palletsprojects.com/en/2.0.x/tutorial/factory/
* motor hat: https://www.waveshare.com/wiki/Motor_Driver_HAT
* ngrok: https://dashboard.ngrok.com/get-started/setup
* https://flask-socketio.readthedocs.io/en/latest/getting_started.html

## Debug
* scan for PI IPs: `arp -na | grep -i b8:27:eb`
* setup wifi: `sudo nano /etc/wpa_supplicant/wpa_supplicant.conf`
* `ssh pi@raspberrypi.local`
