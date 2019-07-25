arr = list();
	
def	listdemo():
	max = 0;
	no = int(input("how many number you went enter:"));
	for i in range(0, no):
		n = int(input("enter element"));
		if (max < n):
			max = n;
		arr.append(int(n));
	return max;
	
ret = listdemo();
print("your Elements is ", arr);
print("max number", ret);

		