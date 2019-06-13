from twython import Twython
from pymongo import MongoClient

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''
dbclient = MongoClient('localhost',27017)
db = dbclient['twitter_data']
collection_tweet = db['tweets']

client = Twython(consumer_key,
                consumer_secret,
                access_token,
                access_secret)

results = client.search(q='tesla',count=100)

collection_tweet.insert_one(results)
#search tweets "lang = en"
for x in collection_tweet.find({},{"lang = en":1}):
    print (x)
sum = 0
x = list(collection_tweet.aggregate(
    [
        {
            '$group' :
            {'_id' : 1,
            'total_retweet': {'$sum':'$retweet_count'}
        }
        }
    ]))
print ("retweet total: {}".format(x[0]['total_retweet']))

x = list(collection_tweet.aggregate(
    [
        {
            '$group' :
            {'_id' : '$user',
            'count': {'$sum':'1'}
        }
        }
    ]))
for y in range(0,len(x)):
    print (x[y])
dbclient.close()
print("Done")