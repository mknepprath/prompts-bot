import os
import time
import json
import random
from urllib import urlopen

import tweepy

class TwitterAPI:
    """
    Class for accessing the Twitter API.
    """
    def __init__(self):
        consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
        consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
        access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message):
        """Send a tweet"""
        self.api.update_status(status=message)

def getTotal():
    LDOCE = urlopen('https://api.pearson.com/v2/dictionaries/ldoce5/entries?apikey=' + os.environ.get('DICT_CONSUMER_KEY')).read().decode('utf8')
    LDOCE_DATA = json.loads(LDOCE)
    return LDOCE_DATA['total']

def getPrompt():
    prompt = ''
    while not prompt.islower() or ' ' in prompt:
        offset = str(random.choice(range(getTotal() - 1)))
        dictionary = urlopen('https://api.pearson.com/v2/dictionaries/ldoce5/entries?offset=' + offset + '&limit=1&apikey=' + os.environ.get('DICT_CONSUMER_KEY')).read().decode('utf8')
        dictData = json.loads(dictionary)
        prompt = dictData['results'][0]['headword']
    return prompt

if __name__ == "__main__":
    twitter = TwitterAPI()
    prompt = getPrompt()
    print 'prompt: ' + prompt

    twitter.tweet(prompt)
