# create a credentials.py file with the following keys
from credentials import ckey, csecret, atoken, asecret
from tweepy import Stream, OAuthHandler
from tweepy.streaming import StreamListener

class listener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=['python'])