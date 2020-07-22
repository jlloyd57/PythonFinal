#!/usr/bin/python

"""
Python Core object Types
"""

import math

def regular_expression_test():  
    ## Given below string, find  all the punctuations in the target list and print the list length.
    target = [';','.',',','–']
    string = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only."
    n_punctuations = 0
    for punctuations in target:
        if punctuations in string:
            n_punctuations += string.count(punctuations)
        n_punctuations

    ###  remove street number from address
    ###  For example,  ‘284–12 West Street’ should become ‘West Street’
    import re
    address = '284-12 West Street'
    address = re.sub(r'^[\d-]+', r'', address)

    print(n_punctuations, address)
    return n_punctuations, address
regular_expression_test()






