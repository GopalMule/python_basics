#!/usr/bin/python
import sys
import test
# A. donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5'
# and donuts(23) returns 'Number of donuts: many'

def donuts(count):
    if count >=10:
        print 'Donuts count: many'
    else:
        print 'Number of donuts',count
    


def main():
    donuts(11)
    donuts(5)
    donuts(0)
    donuts(9)
    donuts(10)
    donuts(100)

if __name__=='__main__':
    main()

