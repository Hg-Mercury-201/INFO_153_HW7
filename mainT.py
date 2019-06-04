import tweepy
import json
from tweepy import OAuthHandler
from pymongo import MongoClient

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
tweets_list = api.search(q="Tesla",count=1, since="2019-01-03")
tweets = tweets_list[0]
json_str = json.dumps(tweets._json)
print(json_str)