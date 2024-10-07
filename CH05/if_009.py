#!/usr/bin/python
###########################################################################################################################
#Multiple list example, to check the availbility of toppings
###########################################################################################################################
available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','fench fries','bell peppers','tomatos','pineapple','olives']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding "+requested_topping.title()+" .")
    else:
        print("Can't add topping "+requested_topping.title()+" as it's not available !!!")

print("Finished making Pizza")
