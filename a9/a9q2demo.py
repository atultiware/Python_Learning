def DisplayFile():

	fd = open("Demo.txt","r")
	print("Info. about File",fd)
	print("contents whole file")
	print(fd.read())
	fd.close()
	
DisplayFile()