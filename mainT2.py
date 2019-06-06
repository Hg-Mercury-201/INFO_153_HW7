import tweepy
from tweepy import OAuthHandler
import json

consumer_key = 'p6tClVvRPB6T8QIXosSNd6zkH'
consumer_secret = 'jNR4VftF0dC7AEVvsePJNOlZOUrERGrQMvopiG8N3TDx95Nbe8'
access_token = '1097916952880779267-FGv9uJYb6PkU8aebe2tCNjQECxJ7gy'
access_secret = 'Gb707a8CRLGCZHxfBzFGEvnIQxn5dMq2iKpdrHL4W4Xq7'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)
tweets = api.search(q="Tesla",count=100)
 
message,favorite_count,retweet_count,created_at,user_name=[],[],[],[],[]
for tweet in tweets:
    message.append(tweet.text)
    favorite_count.append(tweet.favorite_count)
    retweet_count.append(tweet.retweet_count)
    created_at.append(tweet.created_at)
    user_name.append(status.user.name)
    followers_count.append(status.user.followers_count)