file = open("stop-words.txt")
stopwords = file.readlines()
file = open("badwords.txt")
badwords = file.readlines()


name = " "
moodcheck = " "
def removestop(message):
    for word in badwords:
        badword = word.strip()
        message = message.replace( " " + badword + " " , " ")
    for word in stopwords:
         junk = word.strip()
         message = message.replace( " " + junk + " " , " ")
    message = message.replace( " name " , " ")
    return message


def feeling(mood):
    if "not" in mood:
        mood = "Thats to bad i dont realy care"
    elif "good" in mood:
        mood = "thats nice"
    return mood   
    

input = raw_input ("Hi there whats your name: ")
input = " " + input + " "
name = removestop(input)
print("Hello " + name.strip() + " Im chatbot24 nice to meet you")


input = raw_input ("So " + name.strip() +" how are you today:")
input = " " + input + " "
moodcheck = feeling(input) 
print(moodcheck)
