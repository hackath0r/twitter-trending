import json

import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener

import config as cc

consumer_key = cc.consumer_key
consumer_secret = cc.consumer_secret
access_token = cc.access_token
access_token_secret = cc.access_token_secret

INDIA_WOEID = cc.INDIA_WOEID

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitter_api = tweepy.API(auth)


class TweetListener(StreamListener):
    ''' Handles data received from twitter stream. '''
    def on_data(self, data):
        try:
            print data
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_status(self, status):
        print status.__dict__
        return True

    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True # To continue listening

    def on_timeout(self):
        print('Timeout...')
        return True # To continue listening


def get_trending_topics(woeid):
    trends = twitter_api.trends_place(woeid)
    top_trends = trends[0].get("trends", None)

    top_25_trends = top_trends[:25]

    return top_25_trends
