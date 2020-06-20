rows = int(input("Enter the height of the triangle: ").strip())
cols = rows
for row in range(rows):
	for col in range(cols):
		print("{}".format(col+1), end=" ")
	print("")