import serial
import pynmea2
import os
import time
import struct

# time.sleep(20)
serialStream = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)
# serialStream.readline()
while True:
    try:
    	sentence = serialStream.readline()
    	print sentence
#    sentence = sentence.split("$G",1)[-1]
    	if sentence.find('GGA') > 0:
# _       print "$G"+sentence.split("$G",1)[-
        
	        data = pynmea2.parse("$G"+sentence.split("$G",1)[-1])
       		lat = "{lat}".format(lat=data.latitude)
		lon = "{lon}".format(lon=data.longitude)
        	def float_to_hex(f):
           		return hex(struct.unpack('<I', struct.pack('<f', f))[0])

        	hexlon = float_to_hex(float(lon))
        	print "Long= %s" % (lon)
        	hexlat = float_to_hex(float(lat))
        	print "Lat= %s" % (lat)
#        if lon != "0.0" and lat != "0.0":
        	cmdstring = "sudo /home/pi/pi-tracker/ttn-abp \"%s%s\"" % (hexlat[2:10],hexlon[2:10])
        	print cmdstring
        	os.system(cmdstring)

#            cmdstring = "sudo /home/pi/pi-tracker/ttn-otaa \"%s%s\"" % (hexlat[2:10],hexlon[2:10])
#            print cmdstring
#            os.system(cmdstring)
#        	time.sleep(30)
    except Exception:
	print "opps something went wrong "
        time.sleep(30)
    else:
    	time.sleep(30)
