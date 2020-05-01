#!/usr/bin/python

# C. fix_start
# Given a string s, return a string
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.

def fix_start(OrignalString):
    firstchar=OrignalString[0]
    newstring=firstchar.replace(firstchar,'*') + OrignalString[1:]
    print newstring

def main():
    fix_start('babble')
    fix_start('baggle')
    fix_start('aardvark')
    fix_start('google')
    fix_start('donut')
if __name__=='__main__':
    main()

