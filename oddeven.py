# Create a function that counts from 1 to 2000.
# As it loops through each number, have your program generate the number and specify whether it's an odd or even number.
# Ex.: Number is 1.  This is an odd number.

number = 1
msg = "Number is {}. This is an {} number."
numberType = ""

while number < 2001 :
	if number % 2 == 0:
		numberType = "even"
	else:
		numberType = "odd"

	print msg.format(number, numberType)
	number += 1

