arr = list()

def listdemo():
	sum = 0;
	no = int(input("how many number u print: "));
	for i in range(0,no):
		n =int(input("number:"));
		sum = sum + n;
		arr.append(int(n));
	return sum;
		
ret = listdemo();
print("your Elements is ", arr);
print("Addition of list", ret);

