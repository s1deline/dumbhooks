import requests
import time

url = input("enter webhook URL: ")

while True:
    r = requests.post(url, json={"content": "@everyone msg"})
    print(f"sent ({r.status_code})")
    time.sleep(0.1)
