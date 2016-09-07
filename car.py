# Create a class called  Car. In the__init__(), allow the user to specify the following attributes: price, speed, fuel, mileage.
# If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%. 

# Create six different instances of the class Car. In the class have a method called display_all() that returns all
# the information about the car as a string. In your __init__(), call this display_all() method to display information about
# the car once the attributes have been defined.

class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = "15%"
        else:
            self.tax = "12%"
        self.display_all()

    def display_all(self):
        output = "\nPrice: {}\nSpeed: {}\nFuel: {}\nMileage: {}\nTax: {}"
        print output.format(self.price, self.speed, self.fuel, self.mileage, self.tax)

car1 = Car(2000, "35mph", "Full", "15mpg")
car2 = Car(20000, "30mph", "Not Full", "10mpg")
