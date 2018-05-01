#####################################################################################################
# simple class example in which derived classes has their own __init__ methods and also they are
# using base class __init__ method as well by using super
# this is single inheritance so, super is working fine if it would be a multiple inheritance
# then how super works
# e.g class C(A,B):
# in this super will inherit constructor of A. this is called Method resolution order
# or in general it will execute left to right
# one example is given in example3.py file
####################################################################################################


class vehicle(object):
    def __init__(self, name, make, model, price):
        self.name = name
        self.make = make
        self.model = model
        self.price = price

    def vehicle_sound(self):
        return "hummmmm"

class car(vehicle):
    def __init__(self, wheel, name, make, model, price):
        super(car, self).__init__(name, make, model, price)
        self.wheel = wheel


    def display_type(self):
        return "vehicle wheel -- %s" %self.wheel


c = car(4,'honda',2018,'zz',90000)

print c.display_type()
print c.vehicle_sound()
print c.price
