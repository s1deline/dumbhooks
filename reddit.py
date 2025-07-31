import requests
import random
import time

webhook_url = 'INSERT_URL_HERE'

subs = [
    "confessions",
    "TrueOffMyChest",
    "amitheasshole",
    "tifu",
    "offmychest",
    "relationship_advice"
]

headers = {'User-Agent': 'schizoposter/69.0'}

def get_random_post(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=25"
    r = requests.get(url, headers=headers)
    data = r.json()

    posts = data['data']['children']
    random.shuffle(posts)

    for post in posts:
        p = post['data']
        if not p.get('selftext') or len(p['selftext']) < 100: continue

        title = p['title']
        body = p['selftext'].strip()

        if len(body) > 1800:
            body = body[:1800] + '...'

        return f"# {title}\n\n{body}"

    return None

while True:
    sub = random.choice(subs)
    print(f"scraping /r/{sub}")

    post_text = get_random_post(sub)
    if post_text:
        res = requests.post(webhook_url, json={"content": post_text})
        print("sent:", post_text[:60], '...')
    else:
        print("no good posts found")

    time.sleep(10)
