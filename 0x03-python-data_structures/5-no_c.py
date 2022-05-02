#!/usr/bin/python3
def no_c(my_string):
    list1 = list(my_string)
    while ("C" in list1):
        list1.remove("C")
    while ("c" in list1):
        list1.remove("c")
    my_string = ''.join(str(i) for i in list1)
    return(my_string)
