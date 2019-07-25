def countsum(no):

	sum = 0;
	d = 0;
	
	while(no > 0):
		
		#no = no//10;
		d = no % 10;
		no = no // 10;
		sum = sum + d;
	return sum;



no = int(input("Enter the Number:"));
ret = countsum(no);
print("The Number of digit in the number are:",ret);

