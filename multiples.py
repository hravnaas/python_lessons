# part 1
# Create a program that prints all the odd numbers from 1 to 1000. Use the for loop and don't use array to do this exercise.

for number in range(1, 10001):
	if number % 2 != 0:
		print number

# part 2
# Create another program that prints all the multiples of 5 from 5 to 1,000,000.

for number in range(5, 1000001):
	if number % 5 == 0:
		print number