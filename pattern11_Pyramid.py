def pattern10(height):
	for row in range(height, 0, -1):
		for fspc in range(row, height):
			print(" ", end="")
		for starPerRow in range(0, (2*row)-1):
			print("*", end="")
		print("")

if __name__ == "__main__":
	height = int(input("Enter the height of the triangle: "))
	pattern10(height)	