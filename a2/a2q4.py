def addfact(no):
	factorial = 1;
	sum = 0;
	for i in range(1,no):
		if (no % i == 0):
			print(i);
			sum = sum + i;	
	print("factorial sum",sum);

addfact(12);