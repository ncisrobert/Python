import mosquitto, random

client = mosquitto.Mosquitto("DAT205")
client.connect("127.0.0.1")
number = random.random()
print("About to send " + str(number))
client.publish("simon/random", "hello")
