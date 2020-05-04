#!/usr/bin/python

list1=[1,2,2,5]
list2=[]
index=0
length_list=len(list1)
print 'lenght of list', len(list1)

while index<(length_list-1):
    if list1[index]==list1[index+1]:
            list1.pop(index)
            length_list-=1
    index+=1
print list1


'''
for i in range(0,length_list):
    prev=list1[i-1]
    cur=list1[i]
   # next1=list1[i+1]
    
    if prev==cur:
        list1.pop(i)
print list1
                       
'''	
         
