def printevenno(no):
	no2 = no * 2;
	#no3=no2+1;
	for i in range(1,no2+1):
        
		if(i % 2 == 0):
			print(i);
			i += 1;
		else:
			i += 1;
printevenno(10);		
