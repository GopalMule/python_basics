#!/usr/bin/python

# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!

def not_bad(s):
    if 'not' not in s:
        print s
    elif 'not' in s:
        index_of_not=s.find('not')
        if 'bad' not in s[index_of_not:] :
            print s  
        else:
            print s[:index_of_not] + 'good'
    
def main():
    not_bad('This dinner is not that bad!')
    not_bad('This movie is not so bad')
    not_bad('This tea is not hot')
    not_bad("It's bad yet not")

if __name__=='__main__':
    main()

#Output:
#python not_bad.py
'''
This dinner is good
This movie is good
This tea is not hot
It's bad yet not
'''
