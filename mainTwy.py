from twython import Twython
from pymongo import MongoClient

consumer_key = 'p6tClVvRPB6T8QIXosSNd6zkH'
consumer_secret = 'jNR4VftF0dC7AEVvsePJNOlZOUrERGrQMvopiG8N3TDx95Nbe8'
access_token = '1097916952880779267-FGv9uJYb6PkU8aebe2tCNjQECxJ7gy'
access_secret = 'Gb707a8CRLGCZHxfBzFGEvnIQxn5dMq2iKpdrHL4W4Xq7'
dbclient = MongoClient('localhost',27017)
db = dbclient['twitter_data']
collection_tweet = db['tweets']

client = Twython(consumer_key,
                consumer_secret,
                access_token,
                access_secret)

results = client.search(q='tesla',count=100)

collection_tweet.insert_one(results)
dbclient.close()
print("Done")