#!/usr/bin/python
def VariableArgumentDictionaryDemo(a,b,*args,**xargs):
    """riable number of arguments & dictionary """
    print 'Value of a is %d'%a
    print 'Value of b is %d'%b
    for x in args:
        print x
    for x in xargs:
        print x, xargs[x]
VariableArgumentDictionaryDemo(1,2,1,2,3,name="Gopal", Surname="Mule", midlename="Arvind")
VariableArgumentDictionaryDemo(1,2,name="Gopal", Surname="Mule")
