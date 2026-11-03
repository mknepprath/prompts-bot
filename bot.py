import os
import re
import json
import html
import random

from mastodon import Mastodon

RECENT_LIMIT = 100
MAX_ATTEMPTS = 500


def status_text(status):
    # Status content comes back as HTML, e.g. "<p>word</p>".
    text = re.sub(r'<[^>]+>', '', status['content'])
    return html.unescape(text).strip().lower()


def recent_prompts(mastodon):
    statuses = mastodon.account_statuses(mastodon.me()['id'], limit=RECENT_LIMIT)
    return {status_text(s) for s in statuses}


def pick_prompt(words, recent):
    prompt = random.choice(words)
    for _ in range(MAX_ATTEMPTS):
        if prompt.lower() not in recent:
            break
        prompt = random.choice(words)
    return prompt


def main():
    words = json.load(open('words.json'))
    # Skip fragments like "macro-" (issue #5).
    words = [w for w in words if w and w[-1].isalpha()]

    mastodon = Mastodon(
        api_base_url=os.environ.get('MASTODON_BASE_URL'),
        client_id=os.environ.get('MASTODON_CLIENT_KEY'),
        client_secret=os.environ.get('MASTODON_CLIENT_SECRET'),
        access_token=os.environ.get('MASTODON_ACCESS_TOKEN'),
    )

    prompt = pick_prompt(words, recent_prompts(mastodon))

    print('prompt: ' + prompt)

    mastodon.status_post(status=prompt)


if __name__ == "__main__":
    main()
