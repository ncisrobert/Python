import mosquitto
client = mosquitto.Mosquitto("DAT205")
client.connect("127.0.0.1")
client.subscribe("simon/random", 0)
def messageRec(broker, obj, msg):
    global client
    print("Message " + msg.topic + "containing: " + msg.payload)

client.on_message = messageRec
while (client != None): client.loop()
