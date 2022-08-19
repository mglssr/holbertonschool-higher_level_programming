#!/usr/bin/python3
"""Write a Python script that takes in a URL, sends a request
to the URL and displays the value of the X-Request-Id variable
found in the header of the response."""


if __name__ == "__main__":
    from urllib import request
    import sys
    with request.urlopen("{}".format(sys.argv[1])) as resp:
        print(resp.headers['X-Request-Id'])
