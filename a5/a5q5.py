def Asciiavr(str):
    count = 0
    k = 0
    for i in str:
        print(i, ord(i))
        k = k + ord(i)
        count += 1

    ans = k/count
    return ans

strinput = input('Enter string: ')
ret = Asciiavr(strinput)
print('ascii value is : ',ret)