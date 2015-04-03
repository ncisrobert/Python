Python 2.7.9 (default, Dec 10 2014, 12:24:55) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
# Knights to was "ni" video reference
# https://www.youtube.com/watch?v=zIV4poUZAQo

file = open("stop-words.txt")
stopwords = file.readlines()

for word in stopwords:
    next = word.strip()
    print(next)

while True:
    input = raw_input("Say something interesting: ")
    filtered = input.replace(" ni ", " <beep> ")
    print("Your filtered text was: " + filtered)
