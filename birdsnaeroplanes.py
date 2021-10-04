"""
Author: Vincent Scharf
Contact: vincent.scharf@smail.inf.h-brs.de
Description: This very small example should give you an intuitive idea of how abstract
base classes and virtual subclasses work in python
"""

import abc

class Bird(abc.ABC):
    @abc.abstractmethod
    def fly(self):
        pass

class Parrot(Bird):
    def fly(self):
        print("Flying")

p = Parrot()
print("p is Bird?", isinstance(p, Bird))

class Aeroplane(abc.ABC):
    @abc.abstractmethod
    def fly(self):
        pass

class Boeing(Aeroplane):
    def fly(self):
        print("Flying!")

b = Boeing()
print("p is Aeroplane?", isinstance(p, Aeroplane))
print("b is Bird?", isinstance(b, Bird))
