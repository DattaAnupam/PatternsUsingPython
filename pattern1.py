"""
This program prints a simple nxn matrix using python.
This is the 1st program of this "Pattern Printing using python" 
"""
rows = int(input("Enter Number of rows: ").strip())
cols = rows
for row in range(rows):
	for col in range(cols):
		print("*", end=" ")
	print("")