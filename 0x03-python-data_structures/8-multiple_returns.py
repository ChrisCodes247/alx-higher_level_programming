#!/usr/bin/python3

def mutliple_returns(sentence):
    if sentence[0] != None:
        return(len(sentence), sentence[0])
    else:
        return(0, None)
