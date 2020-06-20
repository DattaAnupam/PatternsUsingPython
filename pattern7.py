def pattern7(n, ptrn):
	for row in range(1, n+1):
		for space in range(1, (n-row)+1):
		# Another can be like this: 
		#for space in range(n, row, -1):
			print("", end=" ")
		for col in range(row):
			print(ptrn, end="")
		print()

if __name__ == '__main__':
	n = int(input("Enter the height of triangle: "))
	ptrn = input("Enter a symbol e.g. '*': ")
	pattern7(n, ptrn)