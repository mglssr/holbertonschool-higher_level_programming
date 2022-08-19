#!/usr/bin/python3
"""Write a Python script that takes in a URL, sends a
request to the URL and displays the body of the response."""


if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]
    req = requests.post(url='http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        q_json = req.json()
        if q_json:
            print("[{}] {}".format(q_json['id'], q_json['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
