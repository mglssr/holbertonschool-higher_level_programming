#!/usr/bin/python3
"""Write a Python script that takes in a URL, sends a
request to the URL and displays the body of the response."""


if __name__ == "__main__":
    import requests
    import sys
    user = sys.argv[1]
    passwrd = sys.argv[2]
    url = 'https://api.github.com/user'
    req = requests.get(url, auth=(user, passwrd))
    q_json = req.json()
    if q_json:
        print("{}".format(q_json['id']))
    else:
        print("None")
