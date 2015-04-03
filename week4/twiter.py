import twitter, datetime, sqlite3, urllib2
from bs4 import BeautifulSoup

google = sqlite3.connect("C:\Users\Robert\AppData\Local\Google\Chrome\User Data\Default\History")
cursor = google.cursor()
http = ""
cursor.execute("SELECT * FROM urls")
rows = cursor.fetchall()
data = " "
for line in rows :
    global data 
    data = line[1]
    print data

https = BeautifulSoup(urllib2.urlopen(data))



html = https.title.string[0:]


#cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
#print(cursor.fetchall())

file = open("twiterfile.txt")
cred = file.readline().strip().split(',')

api = twitter.Api(consumer_key=cred[0],consumer_secret=cred[1],access_token_key=cred[2],access_token_secret=cred[3])

timestamp = datetime.datetime.utcnow()

post = "Boom with python the code not the snake Im realy Loveing " + html 

reponse = api.PostUpdate( post )
