#!/usr/bin/python3
"""Write a Python script that fetches
https://intranet.hbtn.io/status"""


if __name__ == "__main__":
    from urllib import request
    with request.urlopen('https://intranet.hbtn.io/status') as resp:
        body = resp.read()
        print(f"Body response:")
        print(f"    - type: {body.get[__class__]}")
        print(f"    - content: {body}")
        print(f"    - utf8 content: {body.decode('utf8')}")
