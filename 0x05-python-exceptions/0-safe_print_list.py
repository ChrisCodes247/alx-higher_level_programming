#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    '''Prints X number of elements in a list.'''
    printed_count = 0
    try:
        i = 0
        while i < x:
            print(my_list[i], end=" ")
            printed_count += 1
            i += 1
    except IndexError:
        pass
    print()
    return printed_count
