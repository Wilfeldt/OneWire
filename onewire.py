#!/usr/bin/python
import time
import paho.mqtt.client as mqtt

broker_address="localhost"
devices_dict = {'28-000005e4e577':'boiler/tank_mid', '28-000005e61d41':'boiler/tank_top', '28-000005e682c8':'boiler/pipe_expansion', '28-000005e7092d':'boiler/tank_bottom', '28-000005e63d4d':'boiler/boiler_return', '28-000005e63cb5':'boiler/tank_forward', '28-000005e63e14':'boiler/boiler_forward','28-000005e7b481': 'boiler/garage_forward', '28-000009fe3214': 'boiler/boiler_heat', '28-000009fe7282': 'boiler/garage_return' }

client = mqtt.Client("broker")

while 1:
        client.connect(broker_address)

        for device in devices_dict:
                tempfile = open("/sys/bus/w1/devices/"+device+"/w1_slave")
                thetext = tempfile.read()
                tempfile.close()
                tempdata = thetext.split("\n")[1].split(" ")[9]
                temp = float(tempdata[2:])
                temp = temp / 1000
                data = "{:.1f}".format(temp)
                client.publish(devices_dict[device],data)

        client.disconnect()
        time.sleep(1)
