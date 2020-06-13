rows = int(input("Enter Number of rows: ").strip())
cols = rows
for row in range(rows):
	for col in range(cols):
		print("{}".format(col+1), end=" ")
	print("")