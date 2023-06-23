#!/usr/bin/python3
""" A function that returns a tuple with the length
    of a string and its first character, if the
    sentence is empty, the first character should be
    equal to none. """


def multiple_returns(sentence):
    if len(sentence) == 0:
        firstCharacter = None
    else:
        firstCharacter = sentence[0]
    newTuple = (len(sentence), firstCharacter)
    return newTuple
