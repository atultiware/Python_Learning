def fact(no):
	factorial = 1;
	
	if no < 0:
		print("number is negative");
		
	elif no == 0:
		print("number is zero");
	
	else:
		for i in range(1,no+1):
			factorial = factorial * i;
		print("factorial is",factorial);
		
fact(5);