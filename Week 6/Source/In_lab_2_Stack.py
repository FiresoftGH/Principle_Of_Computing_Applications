class Customer:
    def __init__(self, name, car):
        self.name = name
        self.car = car
    def __str__(self):
        return f'Your name is {self.name} and your car is {self.car}'

class Reservation(Customer):
    def __init__(self, name, car):
        super().__init__(name, car)

subaru = Customer("Subaru", "Ferrari La Ferrari")
print(subaru.__str__())