
import time
import tweepy
from tweepy.streaming import StreamListener
from .streaming_api import StreamListener

def collect_tweets():
    MONGO_HOST= 'mongodb://localhost/twitterdb'  
    WORDS = ['zappy', 'FictionFone', 'fictionfone', 'Egypt']
#  ['#bigdata', '#AI', '#datascience', '#machinelearning', '#ml', '#iot']
 
    CONSUMER_KEY = "z1bFPfjFkbZKSqTxogxjxVyqN"
    CONSUMER_SECRET = "f9f6z3SH48TDcV4NEke9w7DzbP6gInhfaslLZM8FqCwMHSLJvF"
    ACCESS_TOKEN = "1050811660091514880-0ggSQ1YDhF5yxXXdRmlAeWPPwRm2Lo"
    ACCESS_TOKEN_SECRET = "pmNk57sQzoLbqRIUcpBa25939p8Fa4eWS3GAb2Ec31ODl"
    
    start_time = time.time()
    time_limit = 10

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    #Set up the listener. The 'wait_on_rate_limit=True' is needed to help with Twitter API rate limiting.
    listener = StreamListener(start_time, time_limit) #, wait_on_rate_limit=True 
    streamer = tweepy.Stream(auth=auth, listener=listener)
    print("Tracking: " + str(WORDS))
    streamer.filter(track=WORDS)
    print("done collecting tweets")
