import requests
import sys


def loop():
    for word in sys.stdin:
        res = requests.get(url=f"")
        if res.status_code == 404:
            loop()
        else: 
            data = res.json()
            print(data)
            print(res.status_code)
            print(word)
        # print(res)
        # data = res.json()
        # print(data)
loop()