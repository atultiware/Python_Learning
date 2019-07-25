from threading import *

def forward(no):
    for i in range(no):
        print('forward: ', i+1)

def reverse(no):
    i = no
    while i > 0:
        print('this is reverse: ', i)
        i -= 1

forwardThread = Thread(target=forward, args=(50,))
reverseThread = Thread(target=reverse, args=(50,))

forwardThread.start()
forwardThread.join()
reverseThread.start()

reverseThread.join()

print('main Thread exit')
