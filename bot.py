import os
import json
import random

from mastodon import Mastodon


def main():
    offset = random.choice(range(9998))
    words = json.load(open('words.json'))
    prompt = words[offset]

    print('prompt: ' + prompt)

    mastodon = Mastodon(
        api_base_url=os.environ.get('MASTODON_BASE_URL'),
        client_id=os.environ.get('MASTODON_CLIENT_KEY'),
        client_secret=os.environ.get('MASTODON_CLIENT_SECRET'),
        access_token=os.environ.get('MASTODON_ACCESS_TOKEN'),
    )
    mastodon.status_post(status=prompt)


if __name__ == "__main__":
    main()
