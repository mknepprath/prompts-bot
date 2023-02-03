import os
import json
import random

import tweepy
from mastodon import Mastodon


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


def main():
    offset = random.choice(range(9998))
    words = json.load(open('words.json'))
    prompt = words[offset]

    print('prompt: ' + prompt)

    mastodon = Mastodon(
        api_base_url='https://botsin.space',
        client_id=os.environ.get('MASTODON_CLIENT_KEY'),
        client_secret=os.environ.get('MASTODON_CLIENT_SECRET'),
        access_token=os.environ.get('MASTODON_ACCESS_TOKEN'),
    )
    mastodon.status_post(status=prompt)

    twitter = TwitterAPI()
    twitter.tweet(prompt)

if __name__ == "__main__":
    main()
