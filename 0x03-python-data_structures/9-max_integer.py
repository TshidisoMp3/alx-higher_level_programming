#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    elif len(my_list) == 1:
        return my_list[0]
    else:
        max = my_list[0]
        for i in range(1, len(my_list)):
            if my_list[i] > max:
                max = my_list[i]
        return max
