#!flask/bin/python
from app import *

@app.route('/heatcontrol/gettemp',methods=['GET'])
def getTemperature():
    return jsonify({'temp': 21})
