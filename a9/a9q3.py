from sys import *

def openFile():
    try:
        fd1 = open(argv[1], 'r', encoding ='utf-8')
        fd2 = open('Abc.txt','w+',encoding ='utf-8')
    except IOError as io:
        print('Error in opening file or File does not exist')
    else:
        fd2.write(fd1.read())
        print(fd2.read())
        fd1.close()
        fd2.close()

openFile()