#!/usr/bin/python
import sys, telnetlib, socket, time
from credentials import *

'''

Initial config :
$$$
factory R
set wlan join 1
set wlan ssid xxxx
set wlan passphrase xxxx
save
join
reboot
'''
host=wifly_host
port = wifly_port
tn = telnetlib.Telnet()

#Hacer funcion para obtener la ip del host por la mac address
#de esta forma podemos utilizar ips con dhcp, la mac de wifly
def openConnection():
	try :
		tn.open(host,2000,timeout = 1)
		#print 'Connected to '+ host
	except :
		print 'Unable to connect'

def enterCMDMODE():
	try:
		tn.write("$$$"+"\r")
		time.sleep(1)
	except socket.error:
		print 'Connection already closed'
	try:
		ln = tn.read_very_eager()
	except socket.timeout:
		print 'Socket timeout'

def closeConnection():
	try:
		tn.write("exit"+"\r")
		#print 'Disconnected from '+ host
	except socket.error:
		print 'Connection already closed'
	tn.close()

def execute(command):
	print "EXEC : "+ command
	try:
		tn.write(command+"\r")
		time.sleep(1)
	except socket.error:
		print 'Connection already closed'
	try:
		ln = tn.read_very_eager()
		return ln[len(command+"\r\r\n"):-len("\r\n<4.81> ")]
	except socket.timeout:
		print 'Socket timeout'

def isPinOn(pinNumber):
	varHx = cmd("show io")
	varBin = bin(int(varHx, 16))[2:].zfill(16)[::-1]
	if varBin[pinNumber] == "1":
		return True
	else:
		return False

def getSensorInMv(pinNumber):
	if(pinNumber>7 or pinNumber<0):
		print "Analog interface goes from 0 to 7"
	else:
		varHx = cmd("show q "+str(pinNumber))
		varInt = int(varHx[1:-1],16)/1000
		return varInt

def setPin7On():
	response = cmd("set sys output 0x0080 0x0080")
	if response == "AOK":
		return True
	else:
		return False

def setPin7Off():
	response = cmd("set sys output 0x0000 0x0080")
	if response == "AOK":
		return True
	else:
		return False

def ver():
	print cmd("ver")

def getIP():
	print cmd("get ip a")

def getIO():
	print cmd("show io")

def isPin7UP():
	print isPinOn(7)

def cmd(command):
	openConnection()
	enterCMDMODE()
	response = execute(command)
	closeConnection()
	return response

def triggerPin7(seconds):
	if setPin7On() :
		print "PIN 7 activated -> Waiting "+ str(seconds)+" seconds"
		time.sleep(seconds)
		if setPin7Off():
			print "PIN 7 deactivated after "+ str(seconds)+" seconds"
		else:
			print "Error deactivating PIN 7"
	else : 
		print "Error activating PIN 7"