from graphics import *
import random
import time
from random import randint
counter = 0
datafile = open("data.txt")
data = datafile.read().split() #splits white space into a list
#float(xcor)

window = GraphWin("Onscreen", 500 , 500)

def main():
    window.setBackground(color_rgb(255,255,255))                 

def ball2():
    
    xcor = random.choice(data)
    ball = Circle(Point(randint(0,500),randint(0,500)),25)
    ball.setFill(color_rgb(255-float(xcor),255-float(xcor),255-float(xcor)))
    ball.setOutline(color_rgb(204,207,200))
    ball.draw(window)
        
    

while True:
   
    main()
    ball2()
    counter = counter + 1
    time.sleep(0.3)
    if counter >10:
        xcor = random.choice(data)
        cor = randint(0,10)
        print("printing")
        text = Text(Point(float(xcor)*int(cor),float(xcor)*int(cor)),float(xcor))
        text.draw(window)
        counter = 0   
        
    
    
    
   
