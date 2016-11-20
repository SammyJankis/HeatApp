#!flask/bin/python
from flask import Flask, jsonify
from credentials import *
import netifaces, time

app = Flask(__name__)

@app.route('/heatcontrol/getstate',methods=['GET'])
def getState():
    return jsonify({'state': False})

def is_interface_up(interface):
    addr = netifaces.ifaddresses(interface)
    return netifaces.AF_INET in addr

if __name__ == '__main__':
	while not is_interface_up('wlan0'):
		time.sleep(10)
	app.run(host=rasp_host,port=rasp_port,debug=True)