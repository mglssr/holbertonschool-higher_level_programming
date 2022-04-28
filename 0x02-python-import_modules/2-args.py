#!/usr/bin/python3
import sys
argv = len(sys.argv)
if argv == 2:
    print(f"1 argument:")
    print(f"{1}: {sys.argv[1]}")
elif argv <= 1:
    print(f"0 arguments.")
else:
    print(f"{argv - 1} arguments:")
    for i in range(1, argv):
        print(f"{i}: {sys.argv[i]}")
