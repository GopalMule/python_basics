#!/usr/bin/python

# Addition fof list element
def addlist():
    squares= [1, 4, 7, 8, 10]
    sum = 0
    for num in squares:
        sum=sum+num
    print sum

def main():
    addlist()

if __name__=='__main__':
    main() 
