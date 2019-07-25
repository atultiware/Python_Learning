from itertools import permutations
def Permutation(param):
    permList = permutations(param)
    for perm in list(permList):
        print (''.join(perm))

def toString(List):
    return ''.join(List)
def Permutation3(a, l, r):
    if l == r:
        print(toString(a))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            Permutation3(a, l + 1, r)
            a[l], a[i] = a[i], a[l]

stringInput3 = input('Enter string 3: ')
Permutation(stringInput3)

a = list(stringInput3)
n = len(stringInput3)
Permutation3(a, 0, n-1)