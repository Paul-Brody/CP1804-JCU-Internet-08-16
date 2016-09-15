

"""
CP1404/CP5632 Practical
Client code to use the Car class
Note that the import has a folder (module) in it.
"""
from Prac07.car import Car


def main():
    bus = Car(180, 'bus')
    bus.add_fuel(20)
    bus.drive(30)
    limo = Car(100, 'limo')
    limo.drive(50)
    # print("fuel = bus ", bus.fuel)
    # print("odo bus =", bus.odometer)
    print(bus)
    # print("fuel = limo ", limo.fuel)
    # print("odo = limo ", limo.odometer)
    print(limo)


    # print("Car {}, {}".format(bus.fuel, bus.odometer))
    # print("Car {self.fuel}, {self.odometer}".format(self=bus))
    # print("Car {}, {}".format(bus.fuel, bus.odometer))


if __name__ == "__main__": main()