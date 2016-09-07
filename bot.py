import os
import time
import json
import random
from urllib import urlopen

import tweepy

class TwitterAPI:
    """
    Class for accessing the Twitter API.

    Requires API credentials to be available in environment
    variables. These will be set appropriately if the bot was created
    with init.sh included with the heroku-twitterbot-starter
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

def getPrompt:
    offset = str(random.choice(range(305423)))
    dictionary = urlopen('https://api.pearson.com/v2/dictionaries/entries?offset=' + offset + '&limit=1&apikey=' + os.environ.get('DICT_CONSUMER_KEY')).read().decode('utf8')
    dictData = json.loads(dictionary)
    return dictData['results'][0]['headword']


def log(rec, s):
    if rec:
        cur.execute("INSERT INTO console (log, time) VALUES (%s, 'now')", (str(s),))
        conn.commit()
        print str(s)
        return
    else:
        pass

if __name__ == "__main__":
    twitter = TwitterAPI()
    prompt = getPrompt()
    console.log(prompt)

    #twitter.tweet("Hello world!") #You probably want to remove this line
    #while True:
        #Send a tweet here!
        #time.sleep(60)
