import requests
import time

webhook_url = "INSERT_URL_HERE"

lyrics = """
insert lyrics
"""

lines = lyrics.strip().split('\n')

for line in lines:
    if line.strip() == "":
        continue
    payload = {"content": line.strip()}
    response = requests.post(webhook_url, json=payload)
    if response.status_code != 204:
        print(f"failed to send: {line} - status code: {response.status_code}")
    time.sleep(1.2)
