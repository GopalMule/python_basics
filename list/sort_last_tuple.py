#!/usr/bin/python

# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.

def sort_last(tuples):
    print tuples, 'Sorted tuple:>>',sorted(tuples,key=last), '\n'
    

def last(tuple_last_element):
    return tuple_last_element[-1] #list1[0][-1]

def main():
    sort_last([(1, 3), (3, 2), (2, 1)])
    sort_last([(2, 3), (1, 2), (3, 1)])
    sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
if __name__=='__main__':
    main()

#Output:
#python sort_last_tuple.py
'''
[(1, 3), (3, 2), (2, 1)] Sorted tuple:>> [(2, 1), (3, 2), (1, 3)] 

[(2, 3), (1, 2), (3, 1)] Sorted tuple:>> [(3, 1), (1, 2), (2, 3)] 

[(1, 7), (1, 3), (3, 4, 5), (2, 2)] Sorted tuple:>> [(2, 2), (1, 3), (3, 4, 5), (1, 7)] 

'''
