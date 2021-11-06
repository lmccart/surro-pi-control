#!/usr/bin/python

from flask import Flask, render_template, Response, json
from flask_cors import CORS
# from Surrogate.PCA9685 import PCA9685
from subprocess import call
import time
import os

# pwm = PCA9685(0x40, debug=False)
# pwm.setPWMFreq(50)

# class MotorDriver():
#     def __init__(self):
#         self.PWMA = 0
#         self.AIN1 = 1
#         self.AIN2 = 2
#         self.PWMB = 5
#         self.BIN1 = 3
#         self.BIN2 = 4

#     def MotorRun(self, motor, speed):
#         if speed > 100:
#             return
#         if(motor == 0):
#             pwm.setDutycycle(self.PWMA, speed)
#             pwm.setLevel(self.AIN1, 0)
#             pwm.setLevel(self.AIN2, 1)
#         else:
#             pwm.setDutycycle(self.PWMB, speed)
#             pwm.setLevel(self.BIN1, 0)
#             pwm.setLevel(self.BIN2, 1)

#     def MotorStop(self, motor):
#         if (motor == 0):
#             pwm.setDutycycle(self.PWMA, 0)
#         else:
#             pwm.setDutycycle(self.PWMB, 0)

# Motor = MotorDriver()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    CORS(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/controls/')
    @app.route('/controls/<name>')
    def controls(name=None):
        return render_template('controls.html', name=name)

    @app.route('/turn/<dir>')
    def turn(dir=None):
        if dir == 'left':
            print('left 2 s')
            # Motor.MotorRun(0, 100)
        else:
            print('right 2 s')
            # Motor.MotorRun(1, 100)
        time.sleep(2)
        # Motor.MotorStop(0)
        # Motor.MotorStop(1)
        data = {
            'success' : True
        }
        js = json.dumps(data)
        resp = Response(js, status=200, mimetype='application/json')

        return resp

    @app.route('/shutdown')
    def shutdown():
        call("sudo shutdown -h now", shell=True)

    @app.route('/reboot')
    def reboot():
        call("sudo reboot -h now", shell=True)

    return app
