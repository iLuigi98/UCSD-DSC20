class Car:
        num_wheels = 4
        gas = 10
        headlights = 2
        size = 'Tiny'

        def __init__(self, make, model):
            self.make = make
            self.model = model
            self.wheels = Car.num_wheels
            self.gas = Car.gas

        def drive(self):
            drive_cost = 10
            if self.wheels < Car.num_wheels:
                print(self.make + ' ' + self.model + ' cannot drive!')
                return
            elif self.gas <= 0:
                print(self.make + ' ' + self.model + ' out of fuel!')
                return
            self.gas -= drive_cost
            print(self.make + ' ' + self.model + ' goes vroom!')

        def pop_tire(self):
            if self.wheels > 0:
                self.wheels -= 1

        def fill_gas(self):
            add_amount = 20
            self.gas += add_amount
            print('Your car is full.')

class MonsterTruck(Car):
    size = 'Monster'

    def rev(self):
        print('Vroom! This Monster Truck is huge!')

    def drive(self):
        self.rev()
        Car.drive(self)
