import time, serial, mosquitto
ser = serial.Serial("COM6",9600,timeout=2) # COM 6 for windows , MAC might have to change 
client = mosquitto.Mosquitto("DAT205")
client.connect("127.0.0.1")
client.subscribe("simon/lights")
topic = " "
message = " "

def messageRec(broker, obj, msg):
    global client
    global topic
    global message
    message = msg.payload
    if message in ['on','On','ON','oN']: 
        print ("Important Message from "+ msg.topic + " Turn Led " + message)
        ser.write("ON")
    elif message in ['off','Off','OFF','oFF']:
        print ("Important Message from "+ msg.topic + " Turn Led " + message)
        ser.write("OFF")
    else:
        print ("No usable data")
    
client.on_message = messageRec
while (client != None): client.loop()
