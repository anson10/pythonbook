from car import Car

my_new_car = Car("Tesla" , "Roadster" ,2020)
print(my_new_car.descriptive_name())

my_new_car.odometer_reading = 25
my_new_car.read_odometer()