from clearblade.ClearBladeCore import System
from clearblade.ClearBladeCore import cbLogs
from getProcessInfo import getProcessList
import time

# Disable console logging
cbLogs.DEBUG = False
cbLogs.MQTT_DEBUG = False

# my system credentials
SystemKey = "e0b3f8e40ba4879dc5c7e2e7ce1b"
SystemSecret = "E0B3F8E40BA4ADDCAAE4AFA7FB67"

# instance of my system
mySystem = System(SystemKey, SystemSecret)

# Log in as Sulochan
user = "s.acharya1337@gmail.com"
userPass = "testpassword"

# user object of current session
thisUserObject = mySystem.User(user, userPass)

# MQTT object
mqtt = mySystem.Messaging(thisUserObject)

#what to do after connection
def on_connect(client, userdata, flags, rc):
    client.subscribe("analytics")

#what to do after receiving message
def on_message(client, userdata, message):
    #display analytics received from the clearblade IoT code service
    print "Message received from SERVER: \n";
    print "*****************************\n";
    print message.payload
    print "*****************************\n\n";

mqtt.on_connect = on_connect
mqtt.on_message = on_message

#connect to the mqtt broker
mqtt.connect()

#process batch number
batchNo = 0
iter = 0
while True:
    #every 5 seconds, send CPU usage information to the clearblade IoT code service
    if (iter%5 == 0):
        batchNo += 1
        timestamp = time.time()
        timestamp = int(timestamp)
        processes = getProcessList(batchNo, timestamp)
        mqtt.publish("myCPUInfo", processes)
        print "CPU Information sent to the SERVER \n"
    iter+=1
    time.sleep(1)



