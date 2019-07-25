def DisplayFile():
	try:
		fd = open('Demo.txt','r', encoding ='utf-8')
	except IOError as io:
		print('File dose not exists:')
		#data = fd.read()
	else:
		print('File exists:')
		print(fd)
		data = fd.read()
		print('File Data is:',data)
		fd.close()

DisplayFile()