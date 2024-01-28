#!/usr/bin/python3

def mutliple_returns(sentence):
    if sentence == "":
        return (0, None)
    return(len(sentence), sentence[0])
