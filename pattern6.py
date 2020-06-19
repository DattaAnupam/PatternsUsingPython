def pattern6(n):
	"""
	chr(): method is used to convert to char data type.
	ASCII value of A: 65
	As col will stop before going to 0, we are starting 1 ascii value earlier.
	if for consideration, n = 6, chr(6+64) = chr(70) = 'F'
	"""
	for row in range(n, 0, -1):
		for col in range(0, row):
			print(chr(row+64), end="")
		# for printing new line.
		print()

if __name__ == '__main__':
	n = int(input("Enter base length of the triangle: "))
	pattern6(n)