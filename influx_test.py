import influx
import datetime


def test_write():
    client = influx.InfluxClient()
    t = datetime.datetime.now()
    print t.strftime('%s')
    jsonData = {
        "measurement": "temperature",
        "fields": {
            "value": 11.5
        },
        "tags": {
            "place": "hem"
        }
    }
    series = []
    series.append(jsonData)
    client.writeJson(series)

def test_temp():
    temp = '\nTemp: 12.44'
    t = temp[7:]
    assert(t == '12.44')
