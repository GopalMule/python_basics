#!/usr/bin/python

def sort_dict(dict1):
    for key in sorted(dict1.keys()):
       print  key,':',dict1[key]

def main():
    dict1={'a': 'apple', 'c': 'cat', 'z': 'zebra', 'b': 'banana'}
    sort_dict(dict1)

if __name__=='__main__':
    main()

