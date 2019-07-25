def ReverseString(str):
    # concatenation using for loop
    s1 = ''
    for i in str:
        s1 = i + s1

    # slicing
    s2 = str[::-1]

    # recursion using slicing
    def recursion(s):
        if len(s) == 0:
            return s
        else:
            # print(s, s[1:], s[0], ((s[1:]) + s[0]))
            return recursion(s[1:]) + s[0]
    s3 = recursion(str)

    # revwesed method
    def usereversed(string):
        string = "".join(reversed(string))
        return string
    s4 = usereversed(str)


    return s1,s2,s3,s4


demostr = input('Enter any string to reverse: ')
ret = ReverseString(demostr)

print(ret)
print(type(ret))