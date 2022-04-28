#!/usr/bin/python3
if __name__ == "__main__":
import sys
import add_0 as add

argc = len(sys.argv)
aux = 0

if argc == 2:
    aux = int(sys.argv[1])
elif argc <= 1:
    aux = 0
else:
    for i in range (1, argc):
        aux += int(sys.argv[i])
print(f"{aux}")
