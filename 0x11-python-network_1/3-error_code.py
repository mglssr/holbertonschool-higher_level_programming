#!/usr/bin/python3
"""Write a Python script that takes in a URL,
sends a request to the URL and displays the body
of the response (decoded in utf-8)."""


if __name__ == "__main__":
    from urllib import error, request
    import sys
    try:
        with request.urlopen("{}".format(sys.argv[1])) as resp:
            print(resp.read().decode('utf-8'))
    except error.HTTPError as e:
        print ("Error code: {}".format(e.code))