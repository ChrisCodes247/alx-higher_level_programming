#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    '''deletes a key in a dictionary'''

    if key not in list(a_dictionary):
        return (a_dictionary)
    else:
        del a_dictionary[key]
    return (a_dictionary)