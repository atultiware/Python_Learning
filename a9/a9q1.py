import os
def openfile():
	try:
		fd = os.path.isfile('Demo.txt')
	except IOError as io:
		print('File does not exist')
	else:
		print('File exist')
		#print(fd)
		#fd.close()

openfile()