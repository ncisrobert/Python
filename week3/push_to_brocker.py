import mosquitto, random

client = mosquitto.Mosquitto("DAT205")
client.connect("127.0.0.1")


print("Type a message to the brokcer below")

while True:

    input = raw_input()
    data = input
    if data>0:

        client.publish("simon/lights", str(data))
        print("Your message " + data + " Was Sent ")
        print("Type a message to the brokcer below")
