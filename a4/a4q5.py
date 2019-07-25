from functools import reduce
from chkprimemodul import *
arr = list()
def fun():
    sum1 = 0
    n = int(input('How many Number do you want to enter: '))
    for i in range(0,int(n)):
        no = int(input('Num: '))
        arr.append(int(no))
    return arr
ret = fun()
print('elements are: ', ret)

filtered = list(filter(ChkPrime, arr))
print('filtered elements  are: ', filtered)

modified = list(map(lambda no : (no * 2), filtered))
print('modified elements  are: ', modified)

reduced = reduce(ChkMax, modified)
print('reduced value is: ', reduced)