#import libaires 

import urllib
import bs4
import time
import wikipedia

#open files and put into varibles
file = open("stop-words.txt")
stopwords = file.readlines()

file = open("badwords.txt")
badwords = file.readlines()

qu = open("qestion.txt",'r')
q = qu.readlines()

#make some varibles 
name = " "
moodcheck = " "
gcount = 0
bcount = 0
good = False
first = False
animal = " "
http = "https://en.wikipedia.org/wiki/"
https = ""

#make some functions  
def removestop(message):
    for word in badwords:
        badword = word.strip()
        message = message.replace( " " + badword + " " , "  ")
    for word in stopwords:
         junk = word.strip()
         message = message.replace( " " + junk + " " , " ")
    message = message.replace( " name " , " ")
    message = message.title()
    return message


def feeling(check):
    global gcount
    global bcount
    global good
    if "good" in input: 
        gcount += 1
    if "happy" in input:
        gcount += 1    
    if "fun" in input:
        gcount += 1
    if "well" in input:
        gcount += 1
    if "glad" in input:
        gcount += 1
    if "alright" in input:
        gcount += 1
    if "okay" in input:
        gcount += 1
    if "ok" in input:
        gcount += 1
    if "bad" in input:
        bcount += 1
    if "crap" in input:
        bcount += 1
    if "balls" in input:
        bcount += 1
    if "not" in input:
        bcount += 1
    if "unhappy" in input:
        bcount += 1
    if "no" in input:
        bcount += 1
    if bcount>=gcount:
        check = "What a shame i dont realy care "
        
    else:
        check = "That's nice for you just rub it in why dont you:"
        good = True
    return check

def www(data):
    animal = neww
    https = urllib.urlopen(http + animal)
    data = bs4.BeautifulSoup(https.read())
    return data 

    
#code to run
#first qestion
input = raw_input ("Hi there whats your name: ")
input = " " + input + " "
name = removestop(input)
print("Hello " + name.strip() + " Im chatbot nice to meet you")

#feeling check qestion uses name to strip to talk to user by there name 
input = raw_input ("So " + name.strip() +" how are you today:")
input = " " + input.lower() + " "

moodcheck = feeling(input)

#checking the outcome of feeling test to pick the correct reply
print(moodcheck)
if good == True:
    input = raw_input("Since your haveing such a nice day why dont you tell me you'r favorute animal: ")
else:
    input = raw_input("Id buy you a cake to cheer you up but iv left my wallet in the other directorie so how about you tell me your favoutre animail:")
input = " " + input + " "
# run there answer through web checker functions to get a response 
newwww = removestop(input)
#print (newwww) for deburging
neww = newwww.strip()
#print (neww) for debug
datasend = www(neww)
print ("Well did yu know that : ")+''.join(i + '.' for i in datasend('p')[0].getText().split('.')[:2])
print ("sorry if that took me a while to find put us pythons arnt always the fastest code on the block , ill give you 5 seconds to read that through ")
time.sleep(10)
while True:
    for line in q: 
        input = raw_input("Lets try another , so whats your favroute" + " " + line)
        input = " " + input + " "    
        newwww = removestop(input)
        print (newwww) #for deburging
        neww = newwww.strip()
        print (neww) #for debug
        datasend = wikipedia.summary(neww)
        print '.'.join(datasend.split('.')[:3])
        
        
        


    
    
    
