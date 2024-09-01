#!/usr/bin/python
#######################################################
#EX: A list comprehension allows us to generate the square list
#    in just one line of code. 
#    A list comprehension combines the for loop and the creation of 
#    new elements into one line, and automatically appends each new element.
#    to the list.
#######################################################

squares = [value**2 for value in range(1,11)]
print("The Square of numbers from range(1,11)")
print(squares)
