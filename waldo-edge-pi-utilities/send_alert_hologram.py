from Hologram.HologramCloud import HologramCloud
import datetime
import json


def foundPerson(name, ID, location):
    payload = formatPayload(name, ID, location)
    sendAlert(payload)
    print(payload)

def formatPayload(name, ID, location):
    payloadDict = {}
    payloadDict['name'] = name
    payloadDict['ID'] = ID
    payloadDict['location'] = location
    payloadDict['datetime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    jsonPayload = json.dumps(payloadDict)
    return jsonPayload

def sendAlert(payload):
    hologram = HologramCloud(dict(), network='cellular')

    result = hologram.network.connect()
    if result == False:
        print ' Failed to connect to cell network'

    
    response_code = hologram.sendMessage(payload,
                                    topics=["waldo-edge"])
    print hologram.getResultString(response_code)

    hologram.network.disconnect()