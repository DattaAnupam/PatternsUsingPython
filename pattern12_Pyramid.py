import math

def pattern12(height):
	"""
	Devided the pyramid into two sections for simplicity.
	ptrnmid: It is used to define the mid point of the pyramid. For this point the pyramid is devided.
	math module is used to get the middle row of the pyramid.
	math.ceil(): This method is used to get the upper integer value of the result. eg. if x = 2.67 then math.ceil(x) will give 3
	"""
	# Creating the first part of the pattern.
	ptrnmid = math.ceil(height/2)
	for row in range(1, ptrnmid+1):
		for firstHalf in range(1, row+1):
			print("*", end="")
		print()
	# Creating the second part of the pattern.
	for row in range(ptrnmid, 1, -1):
		for secondHalf in range(1, row):
			print("*", end="")
		print()

if __name__ == '__main__':
	height = int(input("Enter the height of the pyramid: "))
	pattern12(height)