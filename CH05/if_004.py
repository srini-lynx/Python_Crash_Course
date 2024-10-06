#!/usr/bin/python
################################################################
#Example 4: if-elif-else block
#           Including senior citizen over 65 half the price
#           To check the different block change the value of age.
################################################################

age = 4

if age <= 4:
    price = 0
elif age <= 18:
    price = 10
elif age <= 64:
    price = 15
else:
    price = 7

print("The cost of Admission to Amusement Park $"+str(price)+" .")
