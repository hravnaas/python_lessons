class Bike(object):
    def __init__(self, price, max_speed, miles = 0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    # have this method display the bike's price, maximum speed, and the total miles.
    def displayInfo(self):
        print "Price:", self.price
        print "Maximum Speed:", self.max_speed
        print "Total Miles:", self.miles
        return self

    # have it display "Riding" on the screen and increase the total miles ridden by 10
    def ride(self):
        print "Riding"
        self.miles += 10
        return self

    # have it display "Reversing" on the screen and decrease the total miles ridden by 5...
    def reverse(self):
        print "Reversing"
        if self.miles - 5 < 0:
            self.miles = 0
        else:
            self.miles -= 5
        return self

# Have the first instance ride three times, reverse once and have it displayInfo().
print "\nBike 1\n"
Bike(200, "25mph").ride().ride().ride().reverse().displayInfo()

# Have the second instance ride twice, reverse twice and have it displayInfo().
print "\nBike 2\n"
Bike(250, "30mph").ride().ride().reverse().reverse().displayInfo()

# Have the third instance reverse three times and displayInfo().
print "\nBike 3\n"
Bike(300, "40mph").reverse().reverse().reverse().displayInfo()
