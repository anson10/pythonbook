"""A class that can be used to represent a car."""

class Car:
    "A simple attempt to create a car"

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def descriptive_name(self):
        """Returns a neatly descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}" 
        return long_name.title()
    
    def read_odometer(self):
        """Returns the odometer reading""" 
        print(f"The car has ran {self.odometer_reading} miles")

    def update_odometer(self,milage):
        """
        Set the odometer reading to the given value
        Reject the change if it attempts to roll the odometer reading.
        """ 
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You cannot roll back the odometer reading")

    def increment_odometer(self,miles):
        """Add the given amount to odometer reading"""
        self.odometer_reading += miles

    