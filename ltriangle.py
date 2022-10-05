n = 5
for i in range(0,n+1):
 	for j in range(0, n-i+1):
 		print(" ",end="")
 	for j in range(0,i):
 		print("*",end="")
 	print()
