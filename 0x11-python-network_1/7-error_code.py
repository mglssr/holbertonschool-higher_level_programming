#!/usr/bin/python3
"""Write a Python script that takes in a URL, sends a
request to the URL and displays the body of the response."""


if __name__ == "__main__":
    import requests
    import sys
    x = requests.get(sys.argv[1])
    if x.status_code >= 400:
        print("Error code: {}".format(x.status_code))
    else:
        print(x.text)
