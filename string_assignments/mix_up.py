#!/usr/bin/python

def mix_up(s1,s2):
    print s2[:2]+s1[2:] + ' ' + s1[:2]+s2[2:]

def main():
    mix_up('mix', 'pod')
    mix_up('dog', 'dinner')
    mix_up('gnash', 'sport')
    mix_up('pezzy', 'firm')

if __name__=='__main__':
    main()
