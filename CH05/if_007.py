#!/usr/bin/python
#########################################################################################################
#Check for Special Items, availbility and act accordingly
#########################################################################################################

requested_toppings = ['mushrooms','green peppers','extra cheese','tomatos','bell peppers']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Can't add Green Peppers topping , as it's out of stock")
    else:
        print("Adding "+requested_topping+" .")
