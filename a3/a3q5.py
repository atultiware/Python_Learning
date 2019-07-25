from MarvellousNum import *
arr = []

def listprime(no):
	
	
	for i in range(0,no):
		sumprime = 0 ;
		n = int(input("enter elements"));
		arr.append(int(n));

		prime = ChkPrime(n);
		
		if prime != 0 :
			arr.append(prime)
			sumprime = sumprime + prime

			
	return sumprime

no = int(input("How many number you went Enter"));
ret = listprime(no);
print("your Elements is ", arr);


		    	