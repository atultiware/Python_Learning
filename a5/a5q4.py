def RemovePos(param, pos):
    s1 = ''
    j = 0
    print('pos', pos)

    s2 = param[0:pos]
    s3 = param[pos::]
    s4 = s3[1:]

    s5 = s2 + s4
	
    print('first' ,s2)
    print('second' ,s3)
    print('second after trim' ,s4)
    print('append' ,s5)
    return s5

stringInput = input('Enter string: ')
pos = input('Enter pos to delete: ')
ret = RemovePos(stringInput, int(pos))
print(ret)