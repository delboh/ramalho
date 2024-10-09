# Operator overloading in programming refers to the ability to redefine or extend the behavior of existing operators
# when they are used with user-defined types or objects.
# Definition and Purpose
# Operator overloading allows programmers to specify how operators should behave when applied to objects of custom
# classes. It's a form of polymorphism that enables the use of standard operator symbols with user-defined types,
# making code more intuitive and readable12.
# Key Characteristics
# Customized Behavior: It allows operators to have different implementations depending on their operands' types1.
# Syntactic Sugar: Operator overloading is essentially syntactic sugar, providing a more natural syntax for operations
# on custom types.
# Common Use Cases
# Mathematical Objects: Often used in scientific computing to manipulate mathematical objects like complex numbers,
# matrices, or vectors1.
# String Operations: Used for operations like string concatenation2.
# Custom Data Structures:
# Useful for implementing operations on custom data structures like linked lists or trees.

#---------------------------------------------------------
# a Vector class implementing the use of the
# special methods __repr__, __abs__, __add__ and __mul__.
#---------------------------------------------------------
from math import hypot

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

#---------------------------------------------------------
v1 = Vector(2,4)
v2 = Vector(2,1)
v1 + v2
Vector(4, 5)
#---------------------------------------------------------
v = Vector(3, 4)
abs(v)
5.0
#---------------------------------------------------------
v * 3
Vector(9, 12)
abs(v * 3)
15.0
