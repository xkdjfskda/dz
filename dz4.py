class Car:
    def __init__(self, fuel, speed):
        self.fuel = fuel
        self.speed = speed

    def drive(self):
        if self.fuel > 0:
            print('Brrrr')
            self.fuel -= 1
        else:
            print('No fuel!')


class SuperCar(Car):
    def __init__(self, power, fuel, speed):
        super(SuperCar, self).__init__(fuel,speed)
        self.power = power

    def power(self):
        if self.power > 0:
            print('Driving!')
            self.power -= 1
        else:
            print('No Ride')

Wakeful = SuperCar(10, 400, 10000)
Wakeful.drive()