from graphics import *
import random
import time

datafile = open("data.txt")
data = datafile.read().split() #splits white space into a list
#float(xcor)

window = GraphWin("Onscreen", 500 , 500)

def main():
    window.setBackground(color_rgb(255,255,255))
    background = Rectangle(Point(0,0),Point(550,550))
    background.setFill(color_rgb(255,255,255))
    background.draw(window)
    

def ball():
    for  i in range(1000):
        i = i +1
        xcor = random.choice(data)
        ball = Circle(Point(float(xcor)*i,float(xcor)* i),float(xcor)/5)
        ball.setFill(color_rgb(204,207,200))
        ball.setOutline(color_rgb(204,207,200))
        ball.draw(window)

def ball2():
    for  i in range(1000):
        i = i +1
        xcor = random.choice(data)
        ball = Circle(Point(500/i,float(xcor)*i),float(xcor)/5)
        ball.setFill(color_rgb(204,207,200))
        ball.setOutline(color_rgb(204,207,200))
        ball.draw(window)
        
    

while True:
   
    main()
    ball2()
    ball()
    time.sleep(0.3)
    
    
    
   
