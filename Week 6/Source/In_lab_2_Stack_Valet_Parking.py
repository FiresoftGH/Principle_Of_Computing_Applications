import random as rd
import names
import sys

class Customer:
    def __init__(self, name, car):
        self.name = name
        self.car = car

    def __str__(self):
        return f'Customer name is {self.name} and your car is {self.car}'

class Reservation(Customer):
    def __init__(self, name, car):
        super().__init__(name, car)

    def get_lot(self):
        if parking_lot.size() <= 10:
            parking_lot.push([self.name, self.car])
            return parking_lot
        elif parking_lot.size() > 10:
            return f'Parking Lot is full ({parking_lot.size()})'
            
    def get_out(self):
        if parking_lot.size() > 0:
            parking_lot.pop()
        else:
            return f'The Parking Lot is empty'

class Stack:
    def __init__(self, data = []):
        # self.data = deque(data)
        self.data = data
        # Note: For some reason, this required a deque unlike last lab

    def __str__(self):
        return f'Stack is {self.data}'

    def push(self, item):
        # return self.data.appendleft(item)
        return self.data.insert(0, item)

    def pop(self):
        if len(self.data) == 0:
            return "Stack is Empty"
        else:
            return self.data.pop(0)

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

cars = ["Tesla Model Y", "Ferrari La Ferrari", "Toyota Mirai Hybrid", "Ford Everest", "Mazda CX-8", "BMW M1"]
customer = []
for x in range(10):
    customer.append(names.get_first_name())

# Test Case Event

# First Batch of Customers

initial_reservation = [] # This is a normal list (Not a stack)

for index in range(10):
    operation = Reservation(rd.choice(customer), rd.choice(cars))
    initial_reservation.append(operation)
    operation.get_lot()

print(parking_lot)

# The last customer finished their business

print("Pop_test")
initial_reservation[0].get_out()
initial_reservation.pop(0)
print(parking_lot)

# Another user wants to go in the parking lot at any position

print("Pushing Test")
new_guy = Reservation(rd.choice(customer), rd.choice(cars))
new_guy.get_lot()
print(parking_lot)

# Old customers all left
print("More popping")
for customer in initial_reservation:
    customer.get_out()

print(parking_lot)

# New batch of customers came in

print("More pushing")

new_reservation = [] # Again this list is not a stack

new_customer = []
for x in range(10):
    new_customer.append(names.get_first_name())

for index in range(3):
    operation = Reservation(rd.choice(new_customer), rd.choice(cars))
    new_reservation.append(operation)
    operation.get_lot()

print(parking_lot)

# User input
# Comment out these if user input was not needed

choice = ["exit", "enter"]
while True:
    try:
        print(f"Choices: {choice}")
        print(f"Parking Lot: {parking_lot}")
        select = str(input("Input here: "))
        if select not in choice:
            print("Invalid Choice")
        elif select == choice[0]:
            parking_lot.pop()
        elif select == "enter":
            operation = Reservation(names.get_first_name(), rd.choice(cars))
            operation.get_lot()

    except ValueError:
        sys.exit(0)
    
    except KeyboardInterrupt:
        sys.exit(0)

    except TypeError:
        sys.exit(0)
    
            

