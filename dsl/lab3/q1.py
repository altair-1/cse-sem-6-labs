import numpy as np
import pandas as pd
n=int(input("enter a number: "))
print("factors: ")
for i in range(1,n+1):
	if (n%i==0):
		# ic(i)
		print(i)
