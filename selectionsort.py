# Selection Sort

def sort(list):
	if list is None or len(list) < 2:
		# already sorted
		return list

	# Loop through list and keep track of where the unsorted boundary is
	unsortedBoundary = 0
	while unsortedBoundary < len(list):
		smallestIndex = None
		for i in range(unsortedBoundary, len(list)):
			if smallestIndex is None or list[i] < list[smallestIndex]:
				# Store the index of the smallest value in the unsorted area discovered so far
				smallestIndex = i
		
		# If the value at the boundary is not the smallest, swap it for the smallest		
		if smallestIndex != unsortedBoundary:
			temp = list[smallestIndex]
			list[smallestIndex] = list[unsortedBoundary]
			list[unsortedBoundary] = temp

		# Move the boundary up and loop again to process remaining unsorted numbers.
		unsortedBoundary += 1
	
	# The list is now sorted. Return it.
	return list

def printResult(result, expected, prefix):
	if result != expected:
		print prefix, "failed."
		print "\t Expected:", expected
		print "\t Actual:", result
	else:
		print prefix, "passed (" + str(result) + ")"

# Unit tests
printResult(sort({}), {}, "Test 1 - empty list -")
printResult(sort(None), None, "Test 2 - None -")
printResult(sort([1]), [1], "Test 3 - One number -")
printResult(sort([2, 1]), [1, 2], "Test 4 - Two unsorted numbers -")
printResult(sort([1, 2]), [1, 2], "Test 5 - Two sorted numbers -")
printResult(sort([1, 1]), [1, 1], "Test 6 - Two identical numbers -")
printResult(sort([31, 1, 4, 9, 2, 0]), [0, 1, 2, 4, 9, 31], "Test 7 - Several unique unsorted numbers -")
printResult(sort([0, 1, 2, 4, 9, 31]), [0, 1, 2, 4, 9, 31], "Test 8 - Several unique sorted numbers -")
printResult(sort([0, 1, 0, 4, 9, 9, 31]), [0, 0, 1, 4, 9, 9, 31], "Test 9 - Several unsorted numbers with some dupes -")
printResult(sort([1, 1, 1, 1]), [1, 1, 1, 1], "Test 10 - Several identical numbers -")
