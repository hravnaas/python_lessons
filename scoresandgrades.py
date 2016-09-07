# Create a program that prompts the user ten times for a test score between 60 and 100. Each time a score is generated, your program should display what is the grade of that score. Here is the grade table:

# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A

# Scores and Grades
# Score: 87; Your grade is B

def printGrade(score):
	msg = "Score: {}; Your grade is {}"
	if score > 100 or score < 60:
		print "Invalid score -", score
	elif score >= 90:
		print msg.format(score, "A")
	elif score >= 80:
		print msg.format(score, "B")
	elif score >= 70:
		print msg.format(score, "C")
	else:
		print msg.format(score, "D")


numScorePrompts = 10
print "Scores and Grades"

for i in range(0, numScorePrompts):
	# note that raw_input does not work with idle
	score = input("Enter your score (60 - 100): ");
	printGrade(score)
	
print "End of the program. Bye!"

