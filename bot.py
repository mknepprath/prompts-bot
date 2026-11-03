import os
import json
import random
import re

from mastodon import Mastodon


def main():
    words = json.load(open('words.json'))
    # Skip fragments like "macro-" (issue #5).
    words = [w for w in words if re.search(r'[A-Za-z]\Z', w)]
    prompt = random.choice(words)

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
