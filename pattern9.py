def pattern9(n, ptrn, ptrn2):
	for row in range(n, 0, -1):
		for space in range(row, n):
			print("{}".format(ptrn2), end="")
		for col in range(row):
			print(ptrn, end="")
		print()

if __name__ == '__main__':
	n = int(input("Enter the height of triangle: "))
	ptrn = input("Enter the main symbol e.g. '*': ")
	ptrn2 = input("Enter the second symbol except {}: ".format(ptrn))
	pattern9(n, ptrn, ptrn2)