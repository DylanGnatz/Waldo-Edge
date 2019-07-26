from Hologram.HologramCloud import HologramCloud
import datetime
import json

class HologramSender:

    def __init__(self):
        self.hologram = HologramCloud(dict(), network='cellular')
        self.connected = self.hologram.network.connect()
        if self.connected == False:
            print(' Failed to connect to cell network')
    
    def __del__(self):
        self.hologram.network.disconnect()

    def foundPerson(self, name, ID, location):
        payload = self.formatPayload(name, ID, location)
        return self.sendAlert()

    def formatPayload(self, name, ID, location):
        payloadDict = {}
        payloadDict['name'] = name
        payloadDict['ID'] = ID
        payloadDict['location'] = location
        payloadDict['datetime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        jsonPayload = json.dumps(payloadDict)
        self.payload = jsonPayload

    def sendAlert(self):      
        self.responseCode = self.hologram.sendMessage(self.payload,
                                        topics=["waldo-edge"])
        return self.hologram.getResultString(self.responseCode)

        