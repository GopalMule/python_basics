#!/usr/bin/python

# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back

def front_back(a, b):
    len_a=len(a)
    len_b=len(b)
    if len_a%2 ==0:
        print a[:len_a/2] + b[:len_b/2] + a[len_a/2:] + b[len_b/2]

def main():
    front_back('abcd', 'xy')
    front_back('Kitten', 'Donut')
if __name__=='__main__':
    main()

#Output:
#python front_back.py
'''
abxcdy
KitDotenn
'''
