#!/usr/bin/python3
"""Write a Python script that fetches
https://intranet.hbtn.io/status"""


if __name__ == "__main__":
    import urllib
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        body = response.read()
        print(f"Body response:")
        print(f"    - type: {type(body)}")
        print(f"    - content: {body}")
        print(f"    - utf8 content: {body.decode('utf8')}")
