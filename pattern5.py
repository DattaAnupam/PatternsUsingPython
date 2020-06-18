def pattern5(n):
	"""
	n: length of the base of the triangle ie. the max number
		of starts it will contain.
	row range is used to get the exact numbers of rows.
	range():	The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
				range(start, stop, step)
				default for start: 0
				default for step: +1
			So, for row = 1 our second row will start printing col = 6 (let n = 5) and will stop at 2 and not run for 1 as range excludes the stop index and decrease the index by 1.
	"""
	for row in range(1, n+1):
		for col in range(n+1, row, -1):
			print("*", end="")
		print("")
		
if __name__ == '__main__':
	n = int(input(("Enter base length of the triangle: ")))
	pattern5(n)