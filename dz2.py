class Plane:
    def __init__(self, fuel, maxspeed):
        self.fuel = fuel
        self.maxspeed = maxspeed

    def refuel(self, amount):
        self.fuel += amount

    def drive(self):
        if self.fuel > 0:
            print('Flying')
            self.fuel -= 1
        else:
            print("No fuel")


plane = Plane(10, 140)
print(plane.fuel)
print(plane.maxspeed)
plane2 = Plane(15, 290)
print(plane2.fuel)
print(plane2.maxspeed)
print('-------------------')
print(plane.fuel)
plane.refuel(10)
print(plane.fuel)
print('-------------------')
print(plane2.fuel)
plane2.drive()
print(plane2.fuel)