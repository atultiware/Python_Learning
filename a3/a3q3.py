arr = list();
	
def	listdemo():
	#Min 
	no = int(input("how many number you went enter:"));
	for i in range(0, no):
		n = int(input("enter element"));
		arr.append(int(n));
		
		if ( i == 0 ):
			min1 = arr[i];
		
		else:
			min2 = arr[i];
			if ( min2 < min1 ):
				min1 = min2;
	return min1;			
			
ret = listdemo();
print("your Elements is ", arr);
print("Min number", ret);
