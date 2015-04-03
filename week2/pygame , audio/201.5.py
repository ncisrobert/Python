import serial
import pygame
pygame.mixer.init()


def stop():
    sample1.stop()
    sample2.stop()
    sample3.stop()
    sample4.stop()
    sample5.stop()
    sample6.stop()
    sample7.stop()
    sample8.stop()
    sample9.stop()
    sample10.stop()
    sample11.stop()

sample1 = pygame.mixer.Sound("battrey.ogg") 
sample2 = pygame.mixer.Sound("hi.ogg") 
sample3 = pygame.mixer.Sound("mike.ogg") 
sample4 = pygame.mixer.Sound("not.ogg") 
sample5 = pygame.mixer.Sound("pokemon.ogg")
sample6 = pygame.mixer.Sound("rob.ogg") 
sample7 = pygame.mixer.Sound("robots.ogg") 
sample8 = pygame.mixer.Sound("simon.ogg")
sample9 = pygame.mixer.Sound("time.ogg")
sample10 = pygame.mixer.Sound("wallie.ogg")
sample11 = pygame.mixer.Sound("wistle.ogg")
sample12 = pygame.mixer.Sound("shake.ogg")
 



ser = serial.Serial('/dev/ttyACM0',9600)

while True:

    input = ser.readline().strip()

    if(len(input) != 0):
        stop();


	if input == "bat":
		sample1.play()
        	print("Batrrey critical")
        
        if input == "hi":
		sample2.play()
        	print("HI there Whats your name")

        if input == "mike":
		sample3.play()
        	print("Hello Mike")	

        if input == "not":
		sample4.play()
        	print("404 error i reapet 404 ERROR ERROR EROOR 404")

        if input == "pokemon":
		sample5.play()
        	print("Pikachue")

        if input == "rob":
		sample6.play()
        	print("Rob help")

        if input == "robots":
		sample7.play()
        	print("We see EVERYTHING ")

        if input == "simon":
		sample8.play()
        	print("DR.Simon Lock")

        if input == "time":
		sample9.play()
        	print(" Now its time to shake it off")
        	sample12.play()

        if input == "wallie":
		sample10.play()
        	print("WALLIE !!!!!")

        if input == "wistle":
		sample11.play()
        	print("Im Wistleing")	
	
	if input == "stop":
                stop()
        	print("stop all")
		
    		
	
