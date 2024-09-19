#!/usr/bin/python
############################################################
#Example to show the use of 'if' statements in a program
############################################################
cars = [ 'audi', 'bmw', 'lexus', 'rolce roy' ]

print("--------------------------------------------")
print("Contents of cars list ::")
print(cars)
print("--------------------------------------------")
print("Now Cars list Content in formatted way..")
print("--------------------------------------------")
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
print("--------------------------------------------")
