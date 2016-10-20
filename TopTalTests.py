# Test1

def TestFunction(a, n):
	# Function to return array split point, such that count of value 'n' on left side equals count of not 'n' on right side
	length = len(a)
	currentPosition = 0
	
	# get number of n in a
	count = 0
	for value in a:
		if value == n:
			count += 1 
			
	print("Count", count)
	
	# maintain count of n on left, and non-n on right
	# stop when counts are equal
	nOnLeft = 0
	nonNOnRight = length - count
	
	for value in a:
		if nOnLeft == nonNOnRight:
			break
			
		if value == n:
			nOnLeft += 1
		else:	
			nonNOnRight -= 1
	
		currentPosition += 1

		print("currentPosition", currentPosition)
		print("Left", nOnLeft, "Right", nonNOnRight, "\n")

	return currentPosition


# test
x = [2, 4, 7, 4, 8, 4, 5 ,7]

result = TestFunction(x, 4)
print(result)
if result == 5:
	print("Good")
else:
	print("Bad")

