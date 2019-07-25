def chkprime(no):
	flag = 0;
	if no > 1:
	
		for i in range(2,no):
		
			if(no % i ) == 0:
				print("Number is not prime");
				flag = 1;
				break;
		else:
			flag = 0;
			
	if flag == 0:	
		print("Number is prime");
		
	else:
		print("Number is not a prime ");

chkprime(12);
chkprime(5);
chkprime(17);
