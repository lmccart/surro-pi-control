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



## Running
```
$ export FLASK_APP=flaskr
$ export FLASK_ENV=development
$ flask run
```

## References
* flask: https://flask.palletsprojects.com/en/2.0.x/tutorial/factory/
* motor hat: https://www.waveshare.com/wiki/Motor_Driver_HAT
* ngrok: https://dashboard.ngrok.com/get-started/setup
