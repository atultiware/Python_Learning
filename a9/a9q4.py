from sys import *

def SomeFile():
    try:
        fd1 = open(argv[1],'r')
        fd2 = open(argv[2],'r')
    except IOError as io: 
        print('Error in opening File:')
    else:
        t1 = fd1.read()
        t2 = fd2.read()

        if t1 == t2:
            print('some contents:')
        else:
            print('Diff contents:')
        
        fd1.close()
        fd2.close()

    SomeFile()