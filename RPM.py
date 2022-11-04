"Russian Peasant Multiplication"

import pandas as pd
import math

n1 = 89
n2 = 18
print("Multiply ",n1,"x",n2," using 'Russian Peasant Multiplication'")

halving = [n1]
while (min(halving) > 1):
	halving.append(math.floor(min(halving)/2))
print("Halving ",(halving))
	
doubling = [n2]
while(len(doubling) < len(halving)):
	doubling.append(max(doubling) * 2)
print("Doubling", (doubling))
print("Discard even halvings.")
half_double = pd.DataFrame(zip(halving,doubling))
half_double = half_double.loc[half_double[0]%2 == 1,:]
answer = sum(half_double.loc[:,1])

print(half_double)
print("Sum the doubles...")
print("Answer = ",(answer))
