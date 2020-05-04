#!/usr/bin/python
# B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.

def both_ends(s):
    if len(s) <=2:
        print s
    else:
        newstring=s[:2] + s[-2:]
        print newstring 

def main():
    both_ends('Gopal')
    both_ends('aa')
    both_ends('hello')
    both_ends('spring')
    both_ends('xyz')
    both_ends('a')
    
if __name__=='__main__':
    main()

#Output:
#python both_ends.py
'''
Goal
aa
helo
spng
xyyz
a
'''
