#!/usr/bin/python3
"""Write a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)"""


if __name__ == "__main__":
    from urllib import request
    import sys
    data = {'email': "{}".format(sys.argv[2])}
    data = parse.urlencode(data).encode('ascii')

    with request.urlopen(sys.argv[1], data) as response:
        print(response.read().decode('utf-8'))
