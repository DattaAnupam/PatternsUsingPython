def pattern13(height):
	for row in range(height, -(height), -1):
		for space in range(1, abs(row)+1):
			print(" ", end="")
		for col in range(height, abs(row), -1):
			print("* ", end="")
		print()


if __name__ == '__main__':
	height = int(input("Enter the height for the diamond: "))
	pattern13(height)