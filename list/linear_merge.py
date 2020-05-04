#!/usr/bin/python

# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1, list2):
    list1.extend(list2)
    
    print sort_list(list1)
    
def sort_list(list1):
    return sorted(list1)

def main():
    linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
    linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
    linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']) 

if __name__=='__main__':
    main()

#Output:
#python linear_merge.py
'''
['aa', 'bb', 'cc', 'xx', 'zz']
['aa', 'bb', 'cc', 'xx', 'zz']
['aa', 'aa', 'aa', 'bb', 'bb']
'''
