from functools import *
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

filtered1 = list(filter(lambda no : (no % 2 == 0), arr))
print('filtered elements  are: ', filtered1)

modifie1 = list(map(lambda no : (no * no), filtered1))
print('modified elements  are: ', modifie1)

reduced1 = reduce(lambda a,b : a + b, modifie1)
print('reduced value is ', reduced1)