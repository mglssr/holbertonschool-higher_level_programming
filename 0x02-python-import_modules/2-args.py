#!/usr/bin/python3
import sys
argc = len(sys.argv)
if argc == 2:
    print(f"1 argument:")
    print(f"{1}: {sys.argv[1]}")
elif argc <= 1:
    print(f"0 arguments.")
else:
    print(f"{argc - 1} arguments:")
    for i in range(1, argc):
        print(f"{i}: {sys.argv[i]}")
