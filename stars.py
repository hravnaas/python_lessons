def draw_stars(numbers):
	for num in numbers:
		print num * '*'

def draw_stars2(values):
	for val in values:
		if isinstance(val, (str, unicode)):
			print len(val) * val[0].lower()
		else:
			print val * '*'

print "Part 1\n"		
draw_stars([4, 6, 1, 3, 5, 7, 25])

print "\n\nPart 2\n"
draw_stars2([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])