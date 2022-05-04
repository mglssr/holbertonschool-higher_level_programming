#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    s_dic = sorted(a_dictionary)
    for i in range(len(s_dic)):
        print(f"{s_dic[i]}: {a_dictionary.get(s_dic[i])}")
