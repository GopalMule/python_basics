#!/usr/bin/python
# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.

def verbing(s):
    if (len(s)<=2):
        print s
    elif s[-3:]=='ing':
        print s + 'ly'
    else:
        print s + 'ing'
 

def main():
    verbing('swiming')
    verbing('hail')
    verbing('do')
if __name__=='__main__':
    main()

#output:
#python verbing.py
'''
swimingly
hailing
do
'''
