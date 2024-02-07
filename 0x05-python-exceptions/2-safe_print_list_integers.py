#!/usr/bin/python3

def safe_print_list_integers(myList=[], x=0):
    try:
        i = 0
        for a in range(0, x):
            try:
                print("{:d}".format(my_list[a], end=""))
                i += 1
            except (ValueError, TypeError):
                continue
    print("")
    return (i)
