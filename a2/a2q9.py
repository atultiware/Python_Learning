def countnum(no):

	count = 0;
	while(no != 0):
		count = count + 1;
		no = no//10;
		#d = no % 10;
		#no = no / 10;
	return count;
		
		
no = int(input("Enter the Number:"));
ret = countnum(no);
print("The Number of digit in the number are:",ret);