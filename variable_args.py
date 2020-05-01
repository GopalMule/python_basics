#!/usr/bin/python
def VariableArgumentDemo(*args):
    """ Variable Number of Arguments of Demo """
    for x in args:
        print (x)
    else:
        print("We are in elase")
VariableArgumentDemo(1,2,3,4)
VariableArgumentDemo(1,2,3,4,5,6,7,8)
