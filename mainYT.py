import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream

consumer_API = 'p6tClVvRPB6T8QIXosSNd6zkH'
secret_API = 'jNR4VftF0dC7AEVvsePJNOlZOUrERGrQMvopiG8N3TDx95Nbe8'
access = '1097916952880779267-FGv9uJYb6PkU8aebe2tCNjQECxJ7gy'
secret_access = 'Gb707a8CRLGCZHxfBzFGEvnIQxn5dMq2iKpdrHL4W4Xq7'

url = 'https://api.twitter.com/1.1/search/tweets.json'
query = '?q=tesla&count=100'

class TwitterStreamer():

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        listener = StdOutListener(fetched_tweets_filename)
        auth = OAuthHandler(consumer_API,secret_API)
        auth.set_access_token(access,secret_access)

        stream = Stream(auth, listener)

        stream.filter(track = hash_tag_list)

class StdOutListener(StreamListener):
    
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

        def on_error(self,status):
            print(status)

if __name__ == "__main__":

    hash_tag_list = ['elonmusk','tesla','spacex','nasa','model s']
    fetched_tweets_filename = "tweets.json"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)