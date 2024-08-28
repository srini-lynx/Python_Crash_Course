#!/usr/bin/python
#################################################################
#Example Program: To loop through the magicians list and print individual magician
#                 using for loop in this program to demonstrate looping
#################################################################
magicians = [ 'alice', 'david', 'carolina' ]
print("---------------------------------------")
print("Contents of List magicians ::")
print("---------------------------------------")
for magician in magicians:
    print("Magician in title case :: ",magician.title())
print("---------------------------------------")
for magician in magicians:
    print("Magician in Upper case :: ", magician.upper())
print("---------------------------------------")
for magician in magicians:
    print("Magician in lower case :: ", magician.lower())
print("----------------------------------------")
