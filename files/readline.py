#!/usr/bin/python

import sys

def cat(filename):
    f=open(filename, 'rU')    
#    lines=f.readlines()
#    print lines
    print 'read function....'
    text=f.read()
    print text,
    f.close()

def main():
    cat(sys.argv[1]) 

if __name__=='__main__':
    main()   

