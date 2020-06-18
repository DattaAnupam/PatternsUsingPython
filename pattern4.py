def pattern4(n):
	"""
	n: length of the base of the triangle ie. the max number
		of starts it will contain.
	"""
	for row in range(n):
		for col in range(row):
			print("*""", end="")
		print("")
if __name__ == '__main__':
	n = int(input(("Enter base length of the triangle: ")))
	pattern4(n)
