from influxdb import InfluxDBClient
import json


class InfluxClient(object):
    def __init__(self):
        self.host = "192.168.1.252"
        self.db = "test"
        self.client = InfluxDBClient(self.host, 8086, 'root', 'root', self.db)
        self.client.switch_database('test')

    def writeJson(self, jsonData):
        val = self.client.write_points(jsonData)
        if val is not True:
            print "Failed to insert"

    def composeResult(temperature):
        jsonData = []
        data = {
            'measurement': 'temperature',
            'fields': {
                'value': temperature
            },
            'tags': {
                'place': 'hemma'
            }
        }
        st = json.dumps(data)
        jsonData.append(st)
        return jsonData
