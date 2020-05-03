#!/usr/bin/python

def pop(list1):
    index=0
    len_list=len(list1)
    print len_list
    while index<len_list:
        if list1[index][0]=='x':
            list1.pop(index)
            #print len(list1)
            #print list1
            len_list-=1
            continue
        index+=1
        #len_list-=1
    return list1

def main():
    print(pop(['aaa', 'bbb', 'ccd', 'acd', 'xaa', 'xbb']))

if __name__=='__main__':
    main()





