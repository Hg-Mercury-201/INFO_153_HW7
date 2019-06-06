import tweepy
import json
from tweepy import OAuthHandler
from pymongo import MongoClient
from bson import json_util

consumer_API = 'p6tClVvRPB6T8QIXosSNd6zkH'
secret_API = 'jNR4VftF0dC7AEVvsePJNOlZOUrERGrQMvopiG8N3TDx95Nbe8'
access = '1097916952880779267-FGv9uJYb6PkU8aebe2tCNjQECxJ7gy'
secret_access = 'Gb707a8CRLGCZHxfBzFGEvnIQxn5dMq2iKpdrHL4W4Xq7'

client = MongoClient('localhost',27017)
db = client['twitter_data']
collection_tweet = db['tweets']

auth = OAuthHandler(consumer_API,secret_API)
auth.set_access_token(access,secret_access)
api = tweepy.API(auth, wait_on_rate_limit=True)
tweets_list = api.search(q="Tesla",count=100, since="2019-01-03")
tweets = tweets_list[0]
print ("This is tweets list 0: \n" + str(tweets))
json_str = json.dumps(tweets._json)
with open('tweets.json', 'w') as outfile: 
    file_data = json.dump(json_str, outfile)
    
# with open('tweets.json') as f:
#     file_data = json.load(f)
#     file_data = json_util.loads(file_data)
collection_tweet.insert_one(file_data)
client.close()
print("Done")
