def pattern6(n):
	for row in range(n, 0, -1):
		for col in range(0, row):
			print(chr(row+64), end="")
		print()

if __name__ == '__main__':
	n = int(input("Enter base length of the triangle: "))
	pattern6(n)