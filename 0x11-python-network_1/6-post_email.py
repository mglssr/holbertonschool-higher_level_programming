#!/usr/bin/python3
"""Write a Python script that takes in a URL
and an email address, sends a POST request to
the passed URL with the email as a parameter, and
finally displays the body of the response."""


if __name__ == "__main__":
    import requests
    import sys

    data = {'email': "{}".format(sys.argv[2])}

    req = requests.post(url=sys.argv[1], data=data)
    print(req.text)
