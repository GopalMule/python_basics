#!/usr/bin/python

# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
def front_x(words):
    index=0
    list1=words
    list2=[]
    len_list1=len(list1)
    print "Orignal List:", list1
    while index < len_list1:
        if list1[index][0]=='x': #Check strings that begin with 'x' first
            list2.append(list1[index])
            list1.pop(index) 
            len_list1-=1
            continue
            
        index+=1
    
    sorted_list2= sorted(list2)
    sorted_list1= sorted(list1)
    sorted_list2.extend(sorted_list1)
    print "Sorted List:", sorted_list2
    print "\n"

def main():
    front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
    front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
    front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
if __name__=='__main__':
    main()

#Output:
#python front_x.py 
'''
Orignal List: ['bbb', 'ccc', 'axx', 'xzz', 'xaa']
Sorted List: ['xaa', 'xzz', 'axx', 'bbb', 'ccc']


Orignal List: ['ccc', 'bbb', 'aaa', 'xcc', 'xaa']
Sorted List: ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']


Orignal List: ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
Sorted List: ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
'''
