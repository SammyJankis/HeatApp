#!flask/bin/python
from flask import Flask, jsonify
from credentials import *
import netifaces, time
from wifly import *
import mysqlcontroller

app = Flask(__name__)

@app.route('/heatcontrol/getradiator',methods=['GET'])
def getRadiator():
	id = request.args.get('id')
	lastregisters = get_last_twenty_registers(id);
    return jsonify({'state': False})

def is_interface_up(interface):
    addr = netifaces.ifaddresses(interface)
    return netifaces.AF_INET in addr

if __name__ == '__main__':
	while not is_interface_up('wlan0'):
		time.sleep(10)
	app.run(host=rasp_host,port=rasp_port,debug=True)