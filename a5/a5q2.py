def wordString(str):
    
	char = 0
	word = 1
	for i in str:
		char = char + 1
		if(i ==' '):
			word = word + 1

	return word

demostr = input('Enter any string : ')
ret = wordString(demostr)


print('The no. of word in string',ret)
#print(type(ret))




