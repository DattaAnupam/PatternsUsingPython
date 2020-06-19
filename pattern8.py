def pattern8(n, ptrn):
	for row in range(n, 0, -1):
		for space in range(row, n):
			print("", end=" ")
		for col in range(row):
			print(ptrn, end="")
		print()

if __name__ == '__main__':
	n = int(input("Enter the base length of triangle: "))
	ptrn = input("Enter a symbol e.g. '*': ")
	pattern8(n, ptrn)