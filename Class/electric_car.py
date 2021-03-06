""" Example of inheritance in Python """
from car import Car


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)


my_tesla = ElectricCar('tesla', 'model s', '2016')
print(my_tesla.get_descriptive_name())
