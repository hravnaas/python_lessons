class MathDojo(object):
	def __init__(self):
		self.result = 0

	def add(self, *values):
		for num in values:
			if type(num) is list or type(num) is tuple:
				for l in num:
					if isinstance(l, int) or isinstance(l, float):
						self.result = self.result + l
			else:
				if isinstance(num, int) or isinstance(num, float):
					self.result = self.result + num
		return self
		
	def subtract(self, *values):
		for num in values:
			if type(num) is list or type(num) is tuple:
				for l in num:
					if isinstance(l, int) or isinstance(l, float):
						self.result = self.result - l
			else:
				if isinstance(num, int) or isinstance(num, float):
					self.result = self.result + num
		return self

	# def isNumber(num):
	# 	return isinstance(l, int) or isinstance(l, float)

# Execute methods

# Part 1
print MathDojo().add(2, 5).add(2).subtract(3, 2).result

# Part 2
print MathDojo().add([1, 'a'], 3, 4).add('dummy', [3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2, 3], [1.1, 2.3]).result

# Part 3
print MathDojo().add([1, 2], 3, 4, (2, 3)).result


