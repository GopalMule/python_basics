#!/usr/bin/python

# D. MixUp
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.


def mix_up(s1,s2):
    print s2[:2]+s1[2:] + ' ' + s1[:2]+s2[2:]

def main():
    mix_up('mix', 'pod')
    mix_up('dog', 'dinner')
    mix_up('gnash', 'sport')
    mix_up('pezzy', 'firm')

if __name__=='__main__':
    main()

#Output
#python mix_up.py
'''
pox mid
dig donner
spash gnort
fizzy perm
'''
