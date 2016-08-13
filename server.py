import serial
import InfluxClient

def publish(influx, line):
    temp = line[7:]
    print line
    json = influx.composeResult(temp)
    influx.writeJson(json)

ser = serial.Serial("/dev/USB0", 9600)
influx = InfluxClient()

while 1:
    line = ser.readlines(sizehint=10)
    (line)
