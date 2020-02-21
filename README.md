# IoT-MQTT-device-client

## About
* An IoT python client based on Python.
* Uses ClearBlade Python SDK to connect to an IoT cloud hosted on ClearBlade IoT Platform.
* This program uses MQTT message to communicate with IoT cloud.
* The program first connects to a MQTT broker.
* This program then sends CPU Usage Information (PID, Mem Usage, Name, TimeStamp) to the cloud.
* It then listens the cloud for analytics as a MQTT message and displays it.

