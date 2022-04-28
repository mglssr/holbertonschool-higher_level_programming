#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    argv = dir(hidden_4)
    for x in argv:
        if not x.startswith("__", 0):
            print(x)
