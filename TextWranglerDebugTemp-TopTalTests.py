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
	
	# maintain count of n on left, and non-n on right
	# stop when counts are equal
	nOnLeft = 0
	nonNOnRight = length - count
	
	while (nOnLeft != nonNOnright):
		if a[currentPosition] == n:
			++nOnLeft
			--nonNOnRight
		++currentPosition	
	
	
	return currentPosition


# test
x = [2, 4, 7, 4, 8, 4, 5 ,7]

result = TestFunction(x, 4)
if result == 4:
	print("Good")
else:
	print("Bad")

