#!/usr/bin/python
################################################################################################################
#Checking if the List is not empty
################################################################################################################

requested_toppings = []

if requested_toppings:
    for topping in requested_toppings:
        print("Adding " + topping+" .")
else:
    print("Are you sure, you need Plain PIZZA!!!")
