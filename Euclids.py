# Example of recursion using Euclid's algorithm

def gcd(x,y):
	larger=max(x,y)
	smaller=min(x,y)
	print(larger)
	print(smaller)
	
	remainder=larger % smaller
	
	if(remainder == 0):
		return(smaller)
		
	if(remainder != 0):
		return(gcd(smaller,remainder))
		

print(gcd(252,105))
