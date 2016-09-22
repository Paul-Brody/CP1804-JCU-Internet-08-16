from Prac08.taxi import Taxi
'''
Create a separate file, test_taxi.py, to try out your taxi
 (don’t write client code in class files).
Write lines of code for each of the following (hint: use the
 methods available in the Taxi class):
1. Create a new taxi with name “Prius 1”, 100 units of fuel and
 price of $1.20/km
2. Drive the taxi 40km and print the details and the current fare
3. Restart the meter (start a new fare) and then drive the car
 100km
4. Print the details and the current fare
Class Variables
Depending on what kind of system you’re modelling with Taxi,
it might make sense that all taxis have the
same price per km. (We don’t want to get into one Prius and
pay $2.20, then find another one was only $1.20.)
So we can use a “class variable”, which is a variable that is
shared between all instances of that class. You
define class variables directly after the class header line
and before any method definitions.
1. Add the class variable price_per_km and set it to 1.2
2. Change the __init__ function so it doesn’t take in the
price_per_km (and also change any client code
that passes in this value).
Note: you can refer to this variable as Taxi.price_per_km,
which explicitly refers to the class variable
shared by any Taxi instances. You can also use self.price_per_km,
 which refers to the instance
variable that may or may not exist... Python looks for the
variable in the object (instance variable), then
if it doesn't find it there it looks up to the class variable,
 then it looks to the parent class...
3. Test your code and see if you get the same output (you should)
'''


def main():
    taxi = Taxi('Prius 1', 100)
    taxi.add_fuel(0)
    taxi.drive(40)

    print(taxi)

if __name__ == "__main__":
    main()
