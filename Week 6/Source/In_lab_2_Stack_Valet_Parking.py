import random as rd
import names
class Customer:
    def __init__(self, name, car, lot):
        self.name = name
        self.car = car
        self.lot = lot

    def __str__(self):
        return f'Customer name is {self.name}, your car is {self.car}, you want to park at {self.lot} lane'

parking_lot = []

class Reservation(Customer):
    def __init__(self, name, car, lot):
        super().__init__(name, car, lot)

    def get_lot(self):
        if len(parking_lot) <= 10:
            parking_lot.append([self.name, self.car])

    def get_out(self):
        pass
        

cars = ["Tesla Model Y", "Ferrari La Ferrari", "Toyota Mirai Hybrid", "Ford Everest", "Mazda CX-8", "Buggy"]
customer = []
for x in range(10):
    customer.append(names.get_first_name())

# First Batch of Customers

initial_reservation = []

for index in range(10):
    operation = Reservation(rd.choice(customer), rd.choice(cars), 0)
    initial_reservation.append(operation)
    operation.get_lot()

print(parking_lot)