#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list:
        result = 0
        aux = set(my_list)
        uniq = list(aux)
        for i in range (len(uniq)):
            result += int(uniq[i])
        return result
