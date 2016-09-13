from underscore import Underscore

# you just created a library with 5 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore

# Map
result = _.map([1,3,8], lambda x: x * 2)
print result

#evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# should return [2, 4, 6] after you finish implementing the code above