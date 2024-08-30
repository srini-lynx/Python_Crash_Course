#!/usr/bin/python
################################################################
#4-1 Pizza: Think of at least three kinds of your favourate pizza. Store in a list, and then use a for loop to
#    print the name of each pizza.
#    ==> Modify for loop to print a sentence using the name of the pizza instead of printing just the name of the pizza.
#        For each pizza you should have one line of output containing a simple statement like I like pepperoni pizza.
#    ==> Add a line at the end of your program, outside the loop, that states how much you like pizza. The output should
#        consists of 3 or more lines about the kind of pizza you like and then an additional sentence, such as ...
#        I really love pizza!
###############################################################

pizzas = [ 'perrperoni', 'veggie' , 'cheese' ]

for pizza in pizzas:
    print("I like "+pizza.upper()+" pizza.")

print("We enjoy really most pizza types such as veggie,mushroom,pepperoni,bellpepper etc.\nIt's really tasty.")
print("Some of it are really available at a descent price !!!")
print("I really love pizza!")
