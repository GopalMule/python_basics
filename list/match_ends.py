#!/usr/bin/python

# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.
def match_ends(words): # words is the list of string
    index=0
    count=0
    while index <len(words):
        if len(words[index])>=2: #Check whether the string length is 2 or more
            # python>>> list[0][0]==list[0][-1]
            if words[index][0]==words[index][-1]:
                count+= 1 
        index+=1
    return count      
        
    

def main():
    print(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']))
    print(match_ends(['', 'x', 'xy', 'xyx', 'xx']))
    print(match_ends(['aaa', 'be', 'abc', 'hello']))
if __name__=='__main__':
    main()



