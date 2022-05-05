#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        num = 0
        denom = 0
        for i in my_list:
            num += (i[0] * i[1])
            denom += i[1]
        return num / denom
    else:
        return 0
