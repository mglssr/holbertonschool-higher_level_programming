#!/usr/bin/python3
"""Write a Python script that fetches
https://intranet.hbtn.io/status"""


if __name__ == "__main__":
    from urllib
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        body = response.read()
        print(f"Body response:")
        print(f"\t- type: {}".format(type(body)))
        print(f"\t- content: {}".format(body))
        print(f"\t- utf8 content: {body.decode('utf8')}".format(body.decode('utf8')))
