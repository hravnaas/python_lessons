def sort(list):
	if list is None or len(list) < 2:
		# already sorted
		return list

	for i in range(1, len(list)):
			val = list[i]
			lookBack = 1
			# Compare the current value (val) to the one left of it.
			# If the left value is greater, swap it for the current value
			# until index 0 has been reached or the left value is not greater.
			while val < list[i - lookBack] and (i - lookBack) >= 0:
				list[(i - lookBack + 1)] = list[i - lookBack]
				lookBack += 1
			else:
				list[i - lookBack + 1] = val

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
