#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    ''' returns a new list with true or false depending on whether
    the integer in the same position is divisible by 2 '''

    new_list = []
    for num in range(len(my_list)):
        if num % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
