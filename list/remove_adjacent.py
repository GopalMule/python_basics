#!/usr/bin/python

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.

def remove_adjacent(nums):
    list1=nums
    index=0
    length_of_list=len(list1)
    print 'Orignal List:', list1
    while index < (length_of_list-1): # It will iterate till list1[-2] & will compare with last element
        if list1[index]==list1[index+1]:
            list1.pop(index)
            length_of_list-=1
            continue            
        index+=1
    return list1

def main():
    print remove_adjacent([1, 2, 2, 3]),'\n' 
    print remove_adjacent([2, 2, 3, 3, 3]), '\n'
    print remove_adjacent([]), '\n'    

if __name__=='__main__':
    main()

#Output:
#python remove_adjacent.py
'''
Orignal List: [1, 2, 2, 3]
[1, 2, 3] 

Orignal List: [2, 2, 3, 3, 3]
[2, 3] 

Orignal List: []
[] 
'''
