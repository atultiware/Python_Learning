arr = list();
	
def	listdemo(no):
	frequency = 0; 
	#no = int(input("how many number you went enter:"));
	
	#Accept List
	for i in range(0, no):

		n = int(input("enter element"));
		arr.append(int(n));
	
	
	#Serach Element
	serach = int(input("Enter the serach number:"));
	
	for j in arr:
		print(j);
		
		
		if j == serach:
			frequency = frequency + 1;
		
		else:
			frequency = 0;
		
	return frequency ;			
	
no = int(input("how many number you went enter:"));
	
ret = listdemo(no);
print("your Elements is ", arr);
print("The number frequency is ", ret);
