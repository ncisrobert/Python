import twitter, datetime
user = 81494950

file = open("twiterfile.txt")
cred = file.readline().strip().split(',')

api = twitter.Api(consumer_key=cred[0],consumer_secret=cred[1],access_token_key=cred[2],access_token_secret=cred[3])

statuses = api.GetUserTimeline(user)
print (statuses[0].text)
