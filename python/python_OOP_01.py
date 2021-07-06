""" Objectives
    creating classes, methods, and variables;
    calling methods;
    getting simple access to instance variables;

Scenario

    create a class representing a mobile phone;
    your class should implement the following methods:
        __init__ expects a number to be passed as an argument; this method stores the number in an instance variable self.number
        turn_on() should return the message 'mobile phone {number} is turned on'. Curly brackets are used to mark the place to insert the object's number variable;
        turn_off() should return the message 'mobile phone is turned off';
        call(number) should return the message 'calling {number}'. Curly brackets are used to mark the place to insert the object's number variable;
    create two objects representing two different mobile phones; assign any random phone numbers to them;
    implement a sequence of method calls on the objects to turn them on, call any number. Print the methods' outcomes;
    turn off both mobiles.
"""

class Mobilephone():

    def __init__(self, number):
        self.number = number

    def turn_on(self):
        print("mobile phone {0} is turned on".format(self.number))

    def turn_off(self):
        print("mobile phone {0} is turned off".format(self.number))
    
    def call(self,no):
        print("calling {0}".format(no))


m1 = Mobilephone(999)
m2 = Mobilephone(100)

m1.turn_on()
m2.turn_on()

m1.call(666)

m1.turn_off()
m2.turn_off()

"""  
Superclass
"""

class Phone():
    counter = 0

    def __init__(self, number):
        self.number = number
        Phone.counter += 1

    def call(self, number):
        message = 'Calling {} using own number {}'.format(number, self.number)
        return message


class FixedPhone(Phone):
    last_SN = 0

    def __init__(self, number):
        super().__init__(number)
        FixedPhone.last_SN += 1
        self.SN = 'FP-{}'.format(FixedPhone.last_SN)

class MobilePhone(Phone):
    last_SN = 0

    def __init__(self, number):
        super().__init__(number)
        MobilePhone.last_SN += 1
        self.SN = 'MP-{}'.format(MobilePhone.last_SN)

print('Total number of phone devices created:', Phone.counter)
print('Creating 2 devices')
fphone = FixedPhone('555-2368')
mphone = MobilePhone('01632-960004')

print('Total number of phone devices created:', Phone.counter)
print('Total number of mobile phones created:', MobilePhone.last_SN)

print(fphone.call('01632-960004'))
print('Fixed phone received "{}" serial number'.format(fphone.SN))
print('Mobile phone received "{}" serial number'.format(mphone.SN))

print("="*80)
"""

Objectives

    creating classes, class and instance variables;
    accessing class and instance variables;

Scenario

Imagine that you receive a task description of an application that monitors the process of apple packaging before the apples are sent to a shop.

A shop owner has asked for 1000 apples, but the total weight limitation cannot exceed 300 units.

Write a code that creates objects representing apples as long as both limitations are met. When any limitation is exceeded, than the packaging process is stopped, and your application should print the number of apple class objects created, and the total weight.

Your application should keep track of two parameters:

    the number of apples processed, stored as a class variable;
    the total weight of the apples processed; stored as a class variable. Assume that each apple's weight is random, and can vary between 0.2 and 0.5 of an imaginary weight unit;

"""


import random


class Package():

    max_apples = 1000
    weight_in_units = 300 - 0.5
    total_apple_weight = 0
    total_apples = 0  

    def __init__(self):
        pass
        
              

    def addApple(self):
        for apple in range(1000):
            if Package.total_apples <= Package.max_apples and Package.total_apple_weight <= Package.weight_in_units:
                self.apple_weight = random.uniform(0.2, 0.5)
                Package.total_apple_weight += self.apple_weight
                Package.total_apples += 1


p1 = Package()
p1.addApple() 
#print(int(Package.total_apple_weight))   
#print(int(Package.total_apples))
print('Total number of apple in this pack equals {:d} and package weight {:.0f}'.format(Package.total_apples,Package.total_apple_weight ))


print("="*80)

"""
Estimated time

30-60 minutes
Level of difficulty

Medium
Objectives

    improving the student's skills in operating with special methods

Scenario

    Create a class representing a time interval;
    the class should implement its own method for addition, subtraction on time interval class objects;
    the class should implement its own method for multiplication of time interval class objects by an integer-type value;
    the __init__ method should be based on keywords to allow accurate and convenient object initialization, but limit it to hours, minutes, and seconds parameters;
    the __str__ method should return an HH:MM:SS string, where HH represents hours, MM represents minutes and SS represents the seconds attributes of the time interval object;
    check the argument type, and in case of a mismatch, raise a TypeError exception.


"""

print("Lab exercise to be done later- https://edube.org/learn/python-advanced-1/lab-1-implementing-core-syntax")

   # adding time intervals, like: add 21 hours 58 minutes 50 seconds to 1hr 45 minutes 22 seconds;
    
class TimeInterval():
    
    
    def __init__(self, h,m,s):
        self.time_in_seconds = (h * 3600) + (m * 60) + s
        
    def __str__(self):
        return (self.time_in_seconds // 3600, (self.time_in_seconds % 3600) // 60, (self.time_in_seconds % 3600) % 60) 

    def __add__(self, h2, m2, s2):
        time_in_seconds = (h2 * 3600) + (m2 * 60) + s2
        new_time_in_seconds = self.time_in_seconds + time_in_seconds 
        return (new_time_in_seconds // 3600, (new_time_in_seconds % 3600) // 60, (new_time_in_seconds % 3600) % 60)
        
    def __sub__(self, h2, m2, s2):
        time_in_seconds = (h2 * 3600) + (m2 * 60) + s2
        new_time_in_seconds = self.time_in_seconds - time_in_seconds
        return (new_time_in_seconds // 3600, (new_time_in_seconds % 3600) // 60, (new_time_in_seconds % 3600) % 60)

        
t1 = TimeInterval(1,45,22)
print(t1.__str__())

print(t1.__add__(21,58,50))

print("="*80)

"""

Estimated time

10-20 minutes
Level of difficulty

Medium
Objectives

    improving the student's skills in operating with special methods

Scenario

    Extend the class implementation prepared in the previous lab to support the addition and subtraction of integers to time interval objects;
    to add an integer to a time interval object means to add seconds;
    to subtract an integer from a time interval object means to remove seconds.


"""

print("Lab exercise to be done later- https://edube.org/learn/python-advanced-1/python-core-syntax-lab-2")

print("="*80)

print("Inheritance and polymorphism — Inheritance is a pillar of OOP")


