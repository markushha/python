# here you'll see all the imports and interactions
# with all the files related to OOP

from classes import Car

good_car = Car("Porsche", "911 Turbo S", 2017, "Black")

good_car.drive()
good_car.stop()

good_car.wheels = 2

print(good_car.wheels)
# in this case, we'll change class parameter for all objects that were created using Car class
Car.wheels = 3
print(Car.wheels)
