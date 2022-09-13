import random as rd
import names

class Stack:
    def __init__(self, data = []):
        self.data = data

    def __str__(self):
        return f'Stack is {self.data}'

    def push(self, item):
        return [item] + self.data

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[0]

    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False
    
    def size(self):
        return len(self.data)

parking_lot = Stack([])

class Customer:
    def __init__(self, name, car, lot):
        self.name = name
        self.car = car
        self.lot = lot

    def __str__(self):
        return f'Customer name is {self.name}, your car is {self.car}, you want to park at {self.lot} lane'

class Reservation(Customer):
    def __init__(self, name, car, lot):
        super().__init__(name, car, lot)

    def get_lot(self):
        if parking_lot.size() <= 10:
            parking_lot.push([self.name, self.car])

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