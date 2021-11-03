#!/usr/bin/python

from flask import Flask, render_template, Response, json
from flask_socketio import SocketIO
from subprocess import call
import time
import os

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY="dev",
    DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
)
socketio = SocketIO(app)


@socketio.on('init')
def handle_init(msg):
    with open("log.txt") as f:
        lines = f.readlines()
        js = json.dumps(lines)
        socketio.emit('log', {'lines': js})


def log(msg=None):
    ts = time.time() #datetime.datetime.now(pytz.timezone("US/Pacific"))
    with open("log.txt", "a") as f:
        line = msg + "," + str(ts) + '\n'
        f.write(line)
    socketio.emit('msg', { 'msg': line })

def success():
    data = { "success" : True }
    js = json.dumps(data)
    resp = Response(js, status=200, mimetype="application/json")
    return resp

@app.route("/get_log")
def get_log(dir=None):
    with open("log.txt") as f:
        lines = f.readlines()
        js = json.dumps(lines)
        resp = Response(js, status=200, mimetype="application/json")
        return resp

@app.route("/controls/")
@app.route("/controls/<name>")
def controls(name=None):
    return render_template("controls.html", name=name)

@app.route("/turn/<dir>")
def turn(dir=None):
    log(dir)
    return success()

@app.route("/shutdown")
def shutdown():
    call("sudo shutdown -h now", shell=True)

@app.route("/reboot")
def reboot():
    call("sudo reboot -h now", shell=True)

@app.route("/clear_log")
def clear_log():
    file = open("log.txt","r+")
    file.truncate(0)
    file.close()
    return success()




if __name__ == '__main__':
    socketio.run(app)