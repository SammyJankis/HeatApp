#!/usr/bin/python
import MySQLdb
from credentials import *
import json

DB_HOST = 'localhost' 
DB_USER = mysql_default_user 
DB_PASS = mysql_user_heatapi_pass
DB_NAME = mysql_db

TB_TEMPREGISTERS = mysql_tb_tempregisters
TB_TEMPREGISTERS_ID = mysql_tb_tempregisters_id
mysql_tb_tempregisters_sensorId="sensorId"
mysql_tb_tempregisters_date="date"
mysql_tb_tempregisters_temp="temp"
mysql_tb_tempregisters_status="status"
 
def run_query(query=''): 
    data = [DB_HOST, DB_USER, DB_PASS, DB_NAME] 
 
    conn = MySQLdb.connect(*data)
    cursor = conn.cursor()
    cursor.execute(query)
 
    if query.upper().startswith('SELECT'): 
        data = cursor.fetchall()
    else: 
        conn.commit()
        data = None 
 
    cursor.close()
    conn.close()
 
    return data

def insert_temp_register(sensorId,date,temp,status):
    query = "INSERT INTO %s (%s,%s,%s,%s,%s) VALUES (NULL,%s,'%s',%s,%s)" % (TB_TEMPREGISTERS,mysql_tb_tempregisters_id,mysql_tb_tempregisters_sensorId,mysql_tb_tempregisters_date,mysql_tb_tempregisters_temp,mysql_tb_tempregisters_status,sensorId,date,temp,status)
    result = run_query(query)
    return json.dumps(result, default=lambda o: o.isoformat() if hasattr(o, 'isoformat') else o)

def get_all_registers():
    query = "SELECT * FROM %s" % (TB_TEMPREGISTERS)
    result = run_query(query)
    return json.dumps(result, default=lambda o: o.isoformat() if hasattr(o, 'isoformat') else o)

def get_last_twenty_registers(sensorId):
    query = "SELECT * FROM %s WHERE %s = %s ORDER BY %s desc LIMIT 20" % (TB_TEMPREGISTERS,mysql_tb_tempregisters_sensorId,sensorId,mysql_tb_tempregisters_date)
    result = run_query(query)
    return json.dumps(result, default=lambda o: o.isoformat() if hasattr(o, 'isoformat') else o)

