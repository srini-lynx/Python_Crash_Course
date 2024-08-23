#!/usr/bin/python
######################################################################
#Examples for Removing elements from list
######################################################################
cars = [ 'hundyai', 'benz', 'toyota', 'buick', 'porsche', 'audi', 'bmw', 'tesla', 'byd', 'mustnag' ]

print("---------------------------------------------------------------------------------")
print("List of Cars")
print("---------------------------------------------------------------------------------")
print(cars)
#Removing any item from the list using del keyword, if we know the position of the element
print("Use del listname [position] to delete the element from the List")
print("For example:: del cars[4] will delete porsche from the cars list")
del cars[4]
print("---------------------------------------------------------------------------------")
print(cars)
print("---------------------------------------------------------------------------------")
#Removing an Item from the list using pop() Method.
#The pop() method by default removes the Last item in a list, but it lets you work with that item after
#removing it. The term pop comes from thinking of a list as a stack of items and popping one 
#item off the top of the stack. In this analogy, the top of a stack corresponds to the end of a list.

print("Before cars.pop(), the contents of cars list")
print(cars)
print("---------------------------------------------------------------------------------")
popped_car = cars.pop()
print("The poped element can be stored in a variable")
print("popped_car :: ", popped_car)
print("Now the cars List contains ::")
print(cars)
print("---------------------------------------------------------------------------------")
print("cars.pop() can be used to remove any item in the list if we know the elements position")
print("Before cars.pop(), we have the below content")
print(cars)
print("----------------------------------------------------------------------------------")
print("After cars.pop(5) now we have the below contents in the list")
too_expensive = cars.pop(5)
print("Now the car list content are ")
print(cars)
print(too_expensive +", "+"is too expensive")

#Sometimes we won't know the position of the value to be removed from the list, instead know the value itself, in that case we can use remove()

print("-----------------------------------------------------------------------------------")
print("Before using cars.remove('buick') list contents are ...")
print(cars)
cars.remove('buick')
print("After removing 'buick' the contents of list cars are ...")
print(cars)
print("-----------------------------------------------------------------------------------")
