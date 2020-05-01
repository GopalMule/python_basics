#!/usr/bin/python

#print("Hello World")

def add(a,b):
    return(a+b)

def sub(a,b=1):
    return(a-b)

def mul(a,b):
    return(a*b)

def div(a,b):
    return(a//b)

def main():
    print("We are in the main class")
    print("Addition is:", add(5,3))
    print("Substraction is:",sub(6,4))
    #print(sub(5))
    print("Multiplication is:",mul(5,4))
print("I am out of main class...Division is",div(10,5))

if __name__=="__main__":
    main()
