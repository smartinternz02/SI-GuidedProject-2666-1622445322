import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "fy2tn2",
        "typeId": "ESP32",
        "deviceId":"12345"
    },
    "auth": {
        "token": "12345678"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    dpar=random.randint(0,50)
    ph=random.randint(6,10)
    temp=random.randint(-20,125)
    myData={'dustparticles':dpar, 'phvalues':ph, 'watertemperature':temp}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(10)
client.disconnect()
