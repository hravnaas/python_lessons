# You're going to create a program that simulates tossing a coin 5,000 times.
# Your program should display how many times the head/tail appears.

import random

def flipCoin():
	if round(random.random()) == 1:
		return "head"
	return "tail"

msg = "Attempt #{}: Throwing a coin... It's a {}! ... Got {} head(s) so far and {} tail(s) so far "
numHeads = 0;
numCoinFlips = 5000;

print "Starting the program..."

for i in range(0, numCoinFlips):
	coin = flipCoin()
	if coin == "head":
		numHeads += 1

	print msg.format(i + 1, coin, numHeads, i + 1  - numHeads)

print "Ending the program, thank you!"