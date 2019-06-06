from twython import Twython
from pymongo import MongoClient
import json, pprint

consumer_API = 'p6tClVvRPB6T8QIXosSNd6zkH'
secret_API = 'jNR4VftF0dC7AEVvsePJNOlZOUrERGrQMvopiG8N3TDx95Nbe8'
access = '1097916952880779267-FGv9uJYb6PkU8aebe2tCNjQECxJ7gy'
secret_access = 'Gb707a8CRLGCZHxfBzFGEvnIQxn5dMq2iKpdrHL4W4Xq7'

dbclient = MongoClient('localhost',27017)
db = dbclient['twitter_data']
collection_tweet = db['tweets']

client = Twython(consumer_API,secret_API,access,secret_access)

results = client.search(q='tesla',count=100)

collection_tweet.insert_one(results)
dbclient.close()
print("Done")