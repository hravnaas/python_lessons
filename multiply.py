# Create a function called 'multiply' that reads each value in the list (e.g. a = [2, 4, 10, 16])
# and returns a list where each value has been multiplied by 5.
# The function should multiply each value in the list by the second argument.

def multiply(arr, multiplier):
	for i in range(0, len(arr)):
		arr[i] *= multiplier
	return arr

myArr = [2, 4, 10, 16]
result = multiply(myArr, 5)
print result