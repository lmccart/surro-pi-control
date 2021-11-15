#!/usr/bin/python

# first time on a new raspberry pi: run `pip install waitress && bash install-server.sh`
# to restart (after editing server.py for example): `sudo systemctl restart server`
# to check status: `systemctl status server`
# to check logs: `journalctl -feu server`

from flask import Flask, render_template, Response, json
from waitress import serve
from PCA9685 import PCA9685
from subprocess import call
import time
import os

# define the class
class MotorDriver():
    def __init__(self):
        self.pwm = PCA9685(0x40, debug=False)
        self.pwm.setPWMFreq(50)
        self.PWMA = 0
        self.AIN1 = 1
        self.AIN2 = 2
        self.PWMB = 5
        self.BIN1 = 3
        self.BIN2 = 4

    def MotorRun(self, motor, speed):
        if speed > 100:
            return
        if(motor == 0):
            self.pwm.setDutycycle(self.PWMA, speed)
            self.pwm.setLevel(self.AIN1, 0)
            self.pwm.setLevel(self.AIN2, 1)
        else:
            self.pwm.setDutycycle(self.PWMB, speed)
            self.pwm.setLevel(self.BIN1, 0)
            self.pwm.setLevel(self.BIN2, 1)

    def MotorStop(self, motor):
        if (motor == 0):
            self.pwm.setDutycycle(self.PWMA, 0)
        else:
            self.pwm.setDutycycle(self.PWMB, 0)

# create and configure the app
Motor = MotorDriver()
app = Flask(__name__)

# define all the routes
@app.route('/controls/')
@app.route('/controls/<name>')
def controls(name=None):
    return render_template('controls.html', name=name)

@app.route('/turn/<dir>')
def turn(dir=None):
    if dir == 'left':
        print('left 2 s')
        Motor.MotorRun(0, 100)
    else:
        print('right 2 s')
        Motor.MotorRun(1, 100)
    time.sleep(2)
    Motor.MotorStop(0)
    Motor.MotorStop(1)
    data = {
        'success' : True
    }
    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')
    return resp
    # return data

@app.route('/shutdown')
def shutdown():
    call("sudo shutdown -h now", shell=True)

@app.route('/reboot')
def reboot():
    call("sudo reboot -h now", shell=True)

serve(app, listen='*:5000')